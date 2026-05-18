# HelioWind Savonius Generator (OpenSCAD)

Tämä projekti generoi parametrisen Savonius-roottorin OpenSCAD-muotoon ja tekee lisäksi 2D-lapapohjan (DXF).

## Tiedostot

- `config.json` – kaikki mitat ja asetukset
- `generate_savonius_scad.py` – lukee konfiguraation ja generoi mallit
- `savonius.scad` – generoitu OpenSCAD-malli
- `output/` – generoitujen tiedostojen kansio
- `blade_template.dxf` – lavan 2D-levityskuva

## Oletusgeometria

- 2 lapaa
- halkaisija 220 mm
- korkeus 460 mm
- kiertokulma 120°
- akselireikä 12 mm
- alumiinilapojen urat päädyissä

## Ajo

```bash
python generate_savonius_scad.py
openscad -o output/savonius.stl output/savonius.scad
```

Ensimmäinen komento luo:
- `savonius.scad`
- `output/savonius.scad`
- `blade_template.dxf`
- `output/blade_template.dxf`

## Muokattavat mitat

Muokkaa tiedostoa `config.json`:

- `diameter_mm`
- `height_mm`
- `twist_deg`
- `blade_width_mm`
- `shaft_hole_diameter_mm`
- `blade_thickness_mm`
- `plate_thickness_mm`
- `slot_depth_mm`
- `slot_clearance_mm`

Näillä arvoilla voi muuttaa roottorin geometriaa ilman koodimuutoksia.
