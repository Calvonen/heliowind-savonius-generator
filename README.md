# HelioWind Savonius Generator

Parametrinen Savonius-roottorigeneraattori, joka luo automaattisesti:

* 3D-tulostettavat päädyt (STL / STEP)
* alumiinilapojen levityskuvat (DXF)
* kokoonpanon preview-mallin
* säädettävän Savonius-geometrian

Projektin tarkoitus on rakentaa visuaalisesti näyttävä, hiljainen ja modulaarinen hybridienergiaveistos, jossa yhdistyvät:

* pystyakselinen Savonius-tuuliturbiini
* aurinkopaneeli
* LED-valaistus
* Energy Core -moduuli
* USB / USB-C / 12V ulostulot

## Tavoitteet

Projektin pitää pystyä:

1. Generoimaan parametrinen Savonius-roottori
2. Luomaan STL-tiedostot 3D-tulostettaville päädyille
3. Luomaan DXF-levityskuvat alumiinilavoille
4. Tukemaan eri halkaisijoita, korkeuksia ja kiertokulmia
5. Mahdollistamaan modulaarinen rakenne
6. Tukemaan keskiakselia ja laakerointia
7. Mahdollistamaan LED-renkaan ja energy core -moduulin integrointi

## Ensimmäinen tavoitegeometria

* halkaisija: 220 mm
* korkeus: 460 mm
* lapojen määrä: 2
* kiertokulma: 120°
* akselireikä: 12 mm
* lapa: 0.8 mm alumiinilevy
* rakenne: 2 moduulia

## Halutut outputit

Projektin pitää generoida:

* top_plate.stl
* bottom_plate.stl
* blade_template.dxf
* assembly_preview.step

## Tekninen toteutus

Toteutus Pythonilla.

Suositeltu ympäristö:

* FreeCAD Python API
* OpenSCAD
* tai Fusion 360 scripting API

## Tärkeät ominaisuudet

* smooth lofted blade geometry
* developable blade surfaces
* laser-cuttable blade templates
* printable end plates
* configurable dimensions via config.json
* modular stacking support
* hidden screw mounting
* blade slot system for aluminum blades

## Visuaalinen tyyli

Ulkonäön pitäisi olla:

* minimalistinen
* moderni
* hiljainen
* kineettinen
* zen-henkinen
* mattamusta / alumiini

Tavoitteena ei ole maksimaalinen energiantuotto vaan:

* kaunis liike
* hiljainen toiminta
* elegantti tekninen design
* pieni energiantuotto LED-valoille ja elektroniikalle

