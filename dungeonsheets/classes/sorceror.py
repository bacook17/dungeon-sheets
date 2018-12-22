from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class DraconicBloodline(SubClass):
    """Your innate magic comes from draconic magic that was mingled with your
    blood or that of your ancestors. Most often, sorcerers with this origin
    trace their descent back to a mighty sorcerer of ancient times who made a
    bargain with a dragon or who might even have claimed a dragon parent. Some
    of these bloodlines are well established in the world, but most are
    obscure. Any given sorcerer could be the first of a new bloodline, as a
    result of a pact or some other exceptional circumstance.

    """
    name = "Draconic Bloodline"
    features_by_level = defaultdict(list)


class WildMagic(SubClass):
    """Your innate magic comes from the wild forces of chaos that underlie the
    order of creation. You might have endured exposure to some form o f raw
    magic, perhaps through a planar portal leading to Limbo, the Elemental
    Planes, or the mysterious Far Realm. Perhaps you were blessed by a powerful
    fey creature or marked by a demon. Or your magic could be a fluke of your
    birth, with no apparent cause or reason. However it came to be, this
    chaotic magic churns within you, waiting for any outlet.

    """
    name = "Wild Magic"
    features_by_level = defaultdict(list)


# XGTE
class DivineSoul(SubClass):
    """Sometimes the spark of magic that fuels a sorcerer comes from a divine
    source that glimmers within the soul. Having such a blessed soul is a sign
    that your innate magic might come from a distant but powerful familial
    connection to a divine being. Perhaps your ances— tor was an angel,
    transformed into a mortal and sent to fight in a god’s name. Or your birth
    might align with an ancient prophecy, marking you as a servant of the gods
    or a chosen vessel of divine magic.

    A Divine Soul, with a natural magnetism, is seen as a threat by some
    religious hierarchies. As an outsider who commands sacred power, a Divine
    Soul can undermine an existing order by claiming a direct tie to the
    divine.

    In some cultures, only those who can claim the power of a Divine Soul may
    command religious power. In these lands, ecclesiastical positions are
    dominated by a few bloodlines and preserved over generations

    """
    name = "Divine Soul"
    features_by_level = defaultdict(list)


class ShadowMagic(SubClass):
    """You are a creature of shadow, for your innate magic comes from the
    Shadowfell itself. You might trace your lineage to an entity from that
    place, or perhaps you were exposed to its fell energy and transformed by
    it.

    The power of shadow magic casts a strange pall over your physical
    presence. The spark of life that sustains you is muffled, as if it
    struggles to remain viable against the dark energy that imbues your
    soul. At your option, you can pick from or roll on the Shadow Sorcerer
    Quirks table to create a quirk for your character

    """
    name = "Shadow Magic"
    features_by_level = defaultdict(list)


class StormSorcery(SubClass):
    """Your innate magic comes from the power of elemental air. Many with this
    power can trace their magic back to a near-death experience caused by the
    Great Rain, but perhaps you were born during a howling gale so powerful
    that folk still tell stories of it, or your lineage might include the
    influence of potent air creatures such as djinn. Whatever the case, the
    magic of the storm permeates your being.

    Storm sorcerers are invaluable members of a ship’s crew. Their magic allows
    them to exert control over wind and weather in their immediate area. Their
    abilities also prove useful in repelling attacks by sahuagin, pirates,
    and other waterborne threats.

    """
    name = "Storm Sorcery"
    features_by_level = defaultdict(list)


class Sorceror(CharClass):
    name = 'Sorceror'
    hit_dice_faces = 6
    saving_throw_proficiencies = ('constitution', 'charisma')
    _proficiencies_text = ('daggers', 'darts', 'slings',
                           'quarterstaffs', 'light crossbows')
    weapon_proficiencies = (weapons.Dagger, weapons.Dart,
                            weapons.Sling, weapons.Quarterstaff,
                            weapons.LightCrossbow)
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ()
    class_skill_choices = ('Arcana', 'Deception', 'Insight',
                           'Intimidation', 'Persuasion', 'Religion')
    features_by_level = defaultdict(list)
    subclasses_available = (DraconicBloodline, WildMagic, DivineSoul,
                            ShadowMagic, StormSorcery)
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (4, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (4, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (4, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (5, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (5, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (5, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (5, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (5, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (5, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (6, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (6, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (6, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (6, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (6, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (6, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (6, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (6, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (6, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (6, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (6, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }