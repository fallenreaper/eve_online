#!/bin/bash


# System IDs
curl https://esi.evetech.net/latest/universe/systems/?datasource=tranquility > system_ids.json
python __init__.py load