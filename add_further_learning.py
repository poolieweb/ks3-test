#!/usr/bin/env python3
"""
Add further_learning links to every question in all JSON question files.
Maps skill_tags to Oak National Academy unit pages and BBC Bitesize KS3 pages.
"""

import json
import glob
import os

OAK = "https://www.thenational.academy/teachers/programmes"
BBC = "https://www.bbc.co.uk/bitesize/subjects"

# BBC Bitesize KS3 subject landing pages (stable, subject-level)
BBC_SCIENCE    = f"{BBC}/z9ddmp3"
BBC_HISTORY    = f"{BBC}/zrw76sg"
BBC_GEOGRAPHY  = f"{BBC}/zvnrq6f"
BBC_COMPUTING  = f"{BBC}/z7tp34j"

# Oak NA base paths per subject
OAK_SCI  = f"{OAK}/science-secondary-ks3/units"
OAK_HIST = f"{OAK}/history-secondary-ks3/units"
OAK_GEO  = f"{OAK}/geography-secondary-ks3/units"
OAK_COMP = f"{OAK}/computing-secondary-ks3/units"

def oak(subject_path, unit_slug):
    return f"{subject_path}/{unit_slug}/lessons"

# ---------------------------------------------------------------------------
# skill_tag → list of {title, url} further_learning entries
# ---------------------------------------------------------------------------
FURTHER_LEARNING = {

    # ── SCIENCE ─────────────────────────────────────────────────────────────

    # Acids & alkalis
    "acids": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "alkalis": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "pH": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "indicators": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "neutralisation": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "salts": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "metal-reactions": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "carbonate-reactions": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "reactivity-series": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "gas-tests": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "safety": [
        {"title": "Understanding Chemical Reactions – Oak National Academy", "url": oak(OAK_SCI, "understanding-chemical-reactions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "concentration": [
        {"title": "Solutions – Oak National Academy", "url": oak(OAK_SCI, "solutions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Waves, light, sound
    "waves": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "sound": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "light": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "amplitude": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "frequency": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "pitch": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "hearing": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "ultrasound": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "transverse-longitudinal": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "reflection": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "refraction": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "colour": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "filters": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "dispersion": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "spectrum": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "electromagnetic-spectrum": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "eye": [
        {"title": "Sound, Light and Vision – Oak National Academy", "url": oak(OAK_SCI, "sound-light-and-vision")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Cells & life processes
    "cells": [
        {"title": "Cells – Oak National Academy", "url": oak(OAK_SCI, "cells")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "gas-exchange": [
        {"title": "Cells – Oak National Academy", "url": oak(OAK_SCI, "cells")},
        {"title": "Breathing and Respiration – Oak National Academy", "url": oak(OAK_SCI, "breathing-and-respiration")},
    ],

    # Digestion
    "digestion": [
        {"title": "Human Digestive System – Oak National Academy", "url": oak(OAK_SCI, "human-digestive-system")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "enzymes": [
        {"title": "Human Digestive System – Oak National Academy", "url": oak(OAK_SCI, "human-digestive-system")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "nutrition": [
        {"title": "Human Digestive System – Oak National Academy", "url": oak(OAK_SCI, "human-digestive-system")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Skeleton & muscles
    "skeleton": [
        {"title": "Human Skeleton and Muscles – Oak National Academy", "url": oak(OAK_SCI, "human-skeleton-and-muscles")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "muscles": [
        {"title": "Human Skeleton and Muscles – Oak National Academy", "url": oak(OAK_SCI, "human-skeleton-and-muscles")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Respiration & health
    "respiration": [
        {"title": "Breathing and Respiration – Oak National Academy", "url": oak(OAK_SCI, "breathing-and-respiration")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "respiratory": [
        {"title": "Breathing and Respiration – Oak National Academy", "url": oak(OAK_SCI, "breathing-and-respiration")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "health": [
        {"title": "Breathing and Respiration – Oak National Academy", "url": oak(OAK_SCI, "breathing-and-respiration")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "drugs": [
        {"title": "Biodiversity – Oak National Academy", "url": oak(OAK_SCI, "biodiversity")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "smoking": [
        {"title": "Breathing and Respiration – Oak National Academy", "url": oak(OAK_SCI, "breathing-and-respiration")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "exercise": [
        {"title": "Human Skeleton and Muscles – Oak National Academy", "url": oak(OAK_SCI, "human-skeleton-and-muscles")},
        {"title": "Breathing and Respiration – Oak National Academy", "url": oak(OAK_SCI, "breathing-and-respiration")},
    ],

    # Separation techniques
    "separating": [
        {"title": "Separation Techniques – Oak National Academy", "url": oak(OAK_SCI, "separation-techniques")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "chromatography": [
        {"title": "Separation Techniques – Oak National Academy", "url": oak(OAK_SCI, "separation-techniques")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "distillation": [
        {"title": "Separation Techniques – Oak National Academy", "url": oak(OAK_SCI, "separation-techniques")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "filtration": [
        {"title": "Separation Techniques – Oak National Academy", "url": oak(OAK_SCI, "separation-techniques")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "evaporation": [
        {"title": "Separation Techniques – Oak National Academy", "url": oak(OAK_SCI, "separation-techniques")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "mixtures": [
        {"title": "Separation Techniques – Oak National Academy", "url": oak(OAK_SCI, "separation-techniques")},
        {"title": "Solutions – Oak National Academy", "url": oak(OAK_SCI, "solutions")},
    ],
    "solutions": [
        {"title": "Solutions – Oak National Academy", "url": oak(OAK_SCI, "solutions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "solubility": [
        {"title": "Solutions – Oak National Academy", "url": oak(OAK_SCI, "solutions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "calculations": [
        {"title": "Solutions – Oak National Academy", "url": oak(OAK_SCI, "solutions")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Atoms & elements
    "atmosphere": [
        {"title": "Atoms, Elements and Compounds – Oak National Academy", "url": oak(OAK_SCI, "atoms-elements-and-compounds")},
        {"title": "Climate Change and Living Sustainably – Oak National Academy", "url": oak(OAK_SCI, "climate-change-and-living-sustainably")},
    ],

    # Climate & environment
    "climate": [
        {"title": "Climate Change and Living Sustainably – Oak National Academy", "url": oak(OAK_SCI, "climate-change-and-living-sustainably")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "climate-change": [
        {"title": "Climate Change and Living Sustainably – Oak National Academy", "url": oak(OAK_SCI, "climate-change-and-living-sustainably")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "greenhouse-effect": [
        {"title": "Climate Change and Living Sustainably – Oak National Academy", "url": oak(OAK_SCI, "climate-change-and-living-sustainably")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "carbon-cycle": [
        {"title": "Climate Change and Living Sustainably – Oak National Academy", "url": oak(OAK_SCI, "climate-change-and-living-sustainably")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Biodiversity & ecosystems
    "fossils": [
        {"title": "Biodiversity – Oak National Academy", "url": oak(OAK_SCI, "biodiversity")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],

    # Rocks (use atoms/compounds as closest match since rocks unit URL not confirmed)
    "igneous": [
        {"title": "Atoms, Elements and Compounds – Oak National Academy", "url": oak(OAK_SCI, "atoms-elements-and-compounds")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "metamorphic": [
        {"title": "Atoms, Elements and Compounds – Oak National Academy", "url": oak(OAK_SCI, "atoms-elements-and-compounds")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "sedimentary": [
        {"title": "Atoms, Elements and Compounds – Oak National Academy", "url": oak(OAK_SCI, "atoms-elements-and-compounds")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "rock-cycle": [
        {"title": "Atoms, Elements and Compounds – Oak National Academy", "url": oak(OAK_SCI, "atoms-elements-and-compounds")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "weathering": [
        {"title": "Atoms, Elements and Compounds – Oak National Academy", "url": oak(OAK_SCI, "atoms-elements-and-compounds")},
        {"title": "Climate Change and Living Sustainably – Oak National Academy", "url": oak(OAK_SCI, "climate-change-and-living-sustainably")},
    ],

    # Solar system & astronomy
    "solar-system": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "stars": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "galaxies": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "universe": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "moon-phases": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "seasons": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "rotation": [
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
        {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE},
    ],
    "gravity": [
        {"title": "Forces – Oak National Academy", "url": oak(OAK_SCI, "forces")},
        {"title": "Our Solar System and Beyond – Oak National Academy", "url": oak(OAK_SCI, "solar-system-and-beyond")},
    ],
    "weight-mass": [
        {"title": "Forces – Oak National Academy", "url": oak(OAK_SCI, "forces")},
        {"title": "Moving by Force – Oak National Academy", "url": oak(OAK_SCI, "moving-by-force")},
    ],
    "energy": [
        {"title": "Moving by Force – Oak National Academy", "url": oak(OAK_SCI, "moving-by-force")},
        {"title": "Heating and Cooling – Oak National Academy", "url": oak(OAK_SCI, "heating-and-cooling")},
    ],

    # ── HISTORY ─────────────────────────────────────────────────────────────

    # Slave trade
    "slave-trade": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "triangular-trade": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "middle-passage": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "plantation": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "abolition": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "resistance": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "liberty-dawn": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "racism": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],

    # British Empire
    "british-empire": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "british-raj": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "colonies": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "imperialism": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "east-india-company": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "jewel-in-crown": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "divide-and-rule": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "mughal-india": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "resources": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],

    # Industrial Revolution
    "industrial-revolution": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "child-labour": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],

    # Stuart era
    "stuart-era": [
        {"title": "The English Civil War – Oak National Academy", "url": oak(OAK_HIST, "the-english-civil-war-what-can-pamphlets-tell-us-about-17th-century-politics")},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "monarchy": [
        {"title": "The English Civil War – Oak National Academy", "url": oak(OAK_HIST, "the-english-civil-war-what-can-pamphlets-tell-us-about-17th-century-politics")},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "witch-craze": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],

    # General history skills
    "interpretations": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "legacy": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "diversity": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "africa": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "age-of-exploration": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],
    "exploration": [
        {"title": "KS3 History Units – Oak National Academy", "url": f"{OAK_HIST}"},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],

    # ── GEOGRAPHY ───────────────────────────────────────────────────────────

    # Population
    "population": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "population-distribution": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "population-density": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "birth-rate": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "death-rate": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "demographic-transition": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "population-pyramid": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "ageing-population": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "youthful-population": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "overpopulation": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "underpopulation": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "population-control": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "migration": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "Cities: What Are They Like to Live In? – Oak National Academy", "url": oak(OAK_GEO, "cities-what-are-they-like-to-live-in")},
    ],
    "push-pull": [
        {"title": "Population: Where Do People Live? – Oak National Academy", "url": oak(OAK_GEO, "population-where-do-people-live")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],

    # Urbanisation & cities
    "urbanisation": [
        {"title": "Cities: What Are They Like to Live In? – Oak National Academy", "url": oak(OAK_GEO, "cities-what-are-they-like-to-live-in")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "rural-urban": [
        {"title": "Cities: What Are They Like to Live In? – Oak National Academy", "url": oak(OAK_GEO, "cities-what-are-they-like-to-live-in")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "informal-settlements": [
        {"title": "Cities: What Are They Like to Live In? – Oak National Academy", "url": oak(OAK_GEO, "cities-what-are-they-like-to-live-in")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "manchester-case-study": [
        {"title": "Cities: What Are They Like to Live In? – Oak National Academy", "url": oak(OAK_GEO, "cities-what-are-they-like-to-live-in")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "cottonopolis": [
        {"title": "Cities: What Are They Like to Live In? – Oak National Academy", "url": oak(OAK_GEO, "cities-what-are-they-like-to-live-in")},
        {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY},
    ],

    # Asia
    "asia-economy": [
        {"title": "China: A Global Superpower – Oak National Academy", "url": oak(OAK_GEO, "china-a-global-superpower")},
        {"title": "India: A Global Superpower – Oak National Academy", "url": oak(OAK_GEO, "india-a-global-superpower")},
    ],
    "asia-diversity": [
        {"title": "India: A Global Superpower – Oak National Academy", "url": oak(OAK_GEO, "india-a-global-superpower")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "china-interdependence": [
        {"title": "China: A Global Superpower – Oak National Academy", "url": oak(OAK_GEO, "china-a-global-superpower")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "karnataka": [
        {"title": "India: A Global Superpower – Oak National Academy", "url": oak(OAK_GEO, "india-a-global-superpower")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "monsoon": [
        {"title": "India: A Global Superpower – Oak National Academy", "url": oak(OAK_GEO, "india-a-global-superpower")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],

    # Biomes & environment
    "biomes": [
        {"title": "Forest Biomes – Oak National Academy", "url": oak(OAK_GEO, "forest-biomes-why-are-forests-so-important")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "deforestation": [
        {"title": "Forest Biomes – Oak National Academy", "url": oak(OAK_GEO, "forest-biomes-why-are-forests-so-important")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "flooding": [
        {"title": "Forest Biomes – Oak National Academy", "url": oak(OAK_GEO, "forest-biomes-why-are-forests-so-important")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],
    "development": [
        {"title": "Globalisation: Is the World Shrinking? – Oak National Academy", "url": oak(OAK_GEO, "globalisation-is-the-world-shrinking")},
        {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY},
    ],

    # ── COMPUTING ────────────────────────────────────────────────────────────

    # Data representation
    "binary": [
        {"title": "Data Representation: Text and Numbers – Oak National Academy", "url": oak(OAK_COMP, "data-representation-text-and-numbers")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "denary": [
        {"title": "Data Representation: Text and Numbers – Oak National Academy", "url": oak(OAK_COMP, "data-representation-text-and-numbers")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "hex": [
        {"title": "Data Representation: Text and Numbers – Oak National Academy", "url": oak(OAK_COMP, "data-representation-text-and-numbers")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "storage": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],

    # Computer systems
    "hardware": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "fde-cycle": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "input-output": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "logic-gates": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "truth-tables": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "machine-code": [
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],

    # Networks
    "networks": [
        {"title": "Computer Networks and Data Transmission – Oak National Academy", "url": oak(OAK_COMP, "computer-networks-and-data-transmission")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "lan": [
        {"title": "Computer Networks and Data Transmission – Oak National Academy", "url": oak(OAK_COMP, "computer-networks-and-data-transmission")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "wan": [
        {"title": "Computer Networks and Data Transmission – Oak National Academy", "url": oak(OAK_COMP, "computer-networks-and-data-transmission")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "routers": [
        {"title": "Computer Networks and Data Transmission – Oak National Academy", "url": oak(OAK_COMP, "computer-networks-and-data-transmission")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],

    # Cybersecurity
    "cyber-security": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "encryption": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "malware": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "phishing": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "social-engineering": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "dos-attack": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "network-security": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "Computer Networks and Data Transmission – Oak National Academy", "url": oak(OAK_COMP, "computer-networks-and-data-transmission")},
    ],
    "two-factor-auth": [
        {"title": "Introduction to Cybersecurity – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-cybersecurity")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],

    # Programming & algorithms
    "algorithms": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "abstraction": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "decomposition": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "pattern-recognition": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "sequence": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "selection": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "iteration": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "variables": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "pseudocode": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "flowcharts": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "debugging": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "testing": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "programming-languages": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "compilers": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "Computer Systems and Data Science – Oak National Academy", "url": oak(OAK_COMP, "computer-systems-and-data-science")},
    ],
    "ide": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],

    # Software development process
    "requirements-analysis": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "documentation": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
    "iterative-development": [
        {"title": "Introduction to Python Programming – Oak National Academy", "url": oak(OAK_COMP, "introduction-to-python-programming")},
        {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING},
    ],
}


def get_further_learning(skill_tags):
    """Get deduplicated further_learning links for a list of skill_tags."""
    seen_urls = set()
    links = []
    for tag in skill_tags:
        for entry in FURTHER_LEARNING.get(tag, []):
            if entry["url"] not in seen_urls:
                seen_urls.add(entry["url"])
                links.append(entry)
    return links


def process_file(path):
    with open(path) as f:
        data = json.load(f)

    is_list = isinstance(data, list)
    qs = data if is_list else data.get("questions", [])
    updated = 0

    for q in qs:
        if not isinstance(q, dict):
            continue
        if q.get("further_learning"):
            continue  # already has links
        tags = q.get("skill_tags", [])
        links = get_further_learning(tags)
        if links:
            q["further_learning"] = links
            updated += 1
        else:
            # fallback: use first tag to determine subject from file path
            subject = path.split("/")[1]
            fallback = {
                "science": [{"title": "KS3 Science – Oak National Academy", "url": f"{OAK_SCI}"}, {"title": "KS3 Science – BBC Bitesize", "url": BBC_SCIENCE}],
                "history": [{"title": "KS3 History – Oak National Academy", "url": f"{OAK_HIST}"}, {"title": "KS3 History – BBC Bitesize", "url": BBC_HISTORY}],
                "geography": [{"title": "KS3 Geography – Oak National Academy", "url": f"{OAK_GEO}"}, {"title": "KS3 Geography – BBC Bitesize", "url": BBC_GEOGRAPHY}],
                "computing": [{"title": "KS3 Computing – Oak National Academy", "url": f"{OAK_COMP}"}, {"title": "KS3 Computing – BBC Bitesize", "url": BBC_COMPUTING}],
            }
            q["further_learning"] = fallback.get(subject, [])
            updated += 1

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return len(qs), updated


def main():
    files = sorted(glob.glob("questions/**/*.json", recursive=True))
    files = [f for f in files if "_index" not in f]
    total_qs = 0
    total_updated = 0
    for path in files:
        qs, updated = process_file(path)
        total_qs += qs
        total_updated += updated
        print(f"  {path}: {updated}/{qs} updated")
    print(f"\nDone: {total_updated}/{total_qs} questions updated across {len(files)} files")


if __name__ == "__main__":
    main()
