#!/usr/bin/python3


""" Module models/review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review """

    place_id = ""
    user_id = ""
    text = ""
