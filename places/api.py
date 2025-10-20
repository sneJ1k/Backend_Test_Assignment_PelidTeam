from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from places.models import Place

app = FastAPI(title="API для карты Артёма")


class ImageOut(BaseModel):
    image: str
    order: int


class PlaceOut(BaseModel):
    id: int
    title: str
    description_short: str
    description_long: str
    lng: float
    lat: float
    images: List[ImageOut]

    model_config = {"from_attributes": True}


class GeoJSONFeature(BaseModel):
    type: str = "Feature"
    properties: dict
    geometry: dict


class GeoJSON(BaseModel):
    type: str = "FeatureCollection"
    features: List[GeoJSONFeature]


@app.get("/places/", response_model=List[PlaceOut])
def get_places():
    places = Place.objects.all()
    return [
        PlaceOut(
            id=place.id,
            title=place.title,
            description_short=place.description_short,
            description_long=place.description_long,
            lng=place.lng,
            lat=place.lat,
            images=[
                ImageOut(image=img.image.url, order=img.order)
                for img in place.images.all()
            ],
        )
        for place in places
    ]


@app.get("/places/{pk}/", response_model=PlaceOut)
def get_place(pk: int):
    try:
        place = Place.objects.get(pk=pk)
        return PlaceOut(
            id=place.id,
            title=place.title,
            description_short=place.description_short,
            description_long=place.description_long,
            lng=place.lng,
            lat=place.lat,
            images=[
                ImageOut(image=img.image.url, order=img.order)
                for img in place.images.all()
            ],
        )
    except Place.DoesNotExist:
        raise HTTPException(status_code=404, detail="Место не найдено")


@app.get("/json/", response_model=GeoJSON)
def get_geojson():
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
                "properties": {
                    "placeId": place.id,
                    "title": place.title,
                    "details": {
                        "description_short": place.description_short,
                        "description_long": place.description_long,
                    },
                },
            }
        )
    return {"type": "FeatureCollection", "features": features}
