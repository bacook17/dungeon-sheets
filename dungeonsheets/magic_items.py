class MagicItem():
    """
    Generic Magic Item. Add description here.

    """
    name = ''
    ac_bonus = 0
    saving_throw_bonus = 0
    skill_check_bonus = 0
    requires_attunement = False
    needs_implementation = False
    other_bonuses = {}
    rarity = ''

    def __init__(self, owner=None):
        self.owner = owner

    def __str__(self):
        return self.name

    def __repr__(self):
        return '\"{:s}\"'.format(str(self))


class RingOfProtection(MagicItem):
    """
    You gain a +1 bonus to AC and Saving Throws while wearing this ring.

    """
    name = "Ring of Protection"
    ac_bonus = 1
    requires_attunement = True
    rarity = 'Rare'


class DecanterOfEndlessWater(MagicItem):
    """This stoppered flask sloshes when shaken, as if it contains water. The
    decanter weighs 2 pounds.

    You can use an action to remove the stopper and speak one of three command
    words, whereupon an amount of fresh water or salt water (your choice) pours
    out of the flask. The water stops pouring out at the start of your next
    turn. Choose from the following options:

    --"Stream" produces 1 gallon of water.

    --"Fountain" produces 5 gallons of water.

    --"Geyser" produces 30 gallons of water that gushes forth in a geyser 30
    feet long and 1 foot wide. As a bonus action while holding the decanter,
    you can aim the geyser at a creature you can see within 30 feet of you. The
    target must succeed on a DC 13 Strength saving throw or take 1d4
    bludgeoning damage and fall prone. Instead of a creature, you can target an
    object that isn't being worn or carried and that weighs no more than 200
    pounds. The object is either knocked over or pushed up to 15 feet away from
    you.

    """
    name = "Decanter of Endless Water"
    rarity = 'Uncommon'


class ToothOfAnimalFriendship(MagicItem):
    """While holding this wolf's tooth, you can expend it's one charge to cast
    Animal Friendship (DC 13) or Speak With Animals. 

    The charge resets at the next Dawn.
    """
    name = "Tooth of Animal Friendship"
    rarity = 'Uncommon'


class CloakOfBillowing(MagicItem):
    """While wearing this cloak, you can use a bonus action to make it billow
    dramatically.

    """
    name = "Cloak of Billowing"
    rarity = "Common"
    

class CapeOfTheMountebank(MagicItem):
    """This cape smells faintly of brimstone. While wearing it, you can use it to
    cast the Dimension Door spell as an action. This property of the cape can't
    be used again until the next dawn.

    When you disappear, you leave behind a cloud of smoke, and you appear in a
    similar cloud of smoke at your destination. The smoke lightly obscures the
    space you left and the space you appear in, and it dissipates at the end of
    your next turn. A light or stronger wind disperses the smoke.

    """
    name = "Cape of the Mountebank"
    rarity = "Rare"
    requires_attunement = True


class EyesOfCharming(MagicItem):
    """These Crystal lenses fit over the eyes. They have 3 Charges. While wearing
    them, you can expend 1 charge as an action to cast the Charm Person spell
    (save DC 13) on a humanoid within 30 feet of you, provided that you and the
    target can see each other. The lenses regain all expended Charges daily at
    dawn.

    """
    name = "Eyes of Charming"
    rarity = "Uncommon"
    requires_attunement = True


class CharlattansDie(MagicItem):
    """Whenever you roll this six—sided die, you can control which number it
    rolls.

    """
    name = "Charlattan's Die"
    rarity = "Common"


class PipeOfSmokeMonsters(MagicItem):
    """While smoking this pipe, you can use an action to ex- hale a puff of smoke
    that takes the form of a single crea— ture, such as a dragon, a flumph, or
    a froghemoth. The form must be small enough to fit in a 1-foot cube and
    loses its shape after a few seconds, becoming an ordi- nary puff of smoke.

    """
    name = 'Pipe of Smoke Monsters'
    rarity = "Common"


class CoinsOfCommunication(MagicItem):
    """This set of multiple coins are virtually indistinguishable from regular Gold
    Pieces, but are connected by magic. Once per day, a holder of any of any
    coin can whisper a single word into it, after which all coins will
    immediately vibrate and the word will replace a word in the traditional
    Kings Message imprinted on the coin. This ability cannot be used again by
    the holder of any of the coins until the following dawn.

    """
    name = "Coins of Communication"
    rarity = "Uncommon"

    
class FlameTongue(MagicItem):
    """You can use a Bonus Action to speak this magic sword's Command Word, causing
    flames to erupt from the blade. These flames shed bright light in a 40-foot
    radius and dim light for an additional 40 feet. While the sword is ablaze,
    it deals an extra 2d6 fire damage to any target it hits. The flames last
    until you use a Bonus Action to speak the Command Word again or until you
    drop or sheathe the sword

    """
    name = "Flame Tongue"
    rarity = "Rare"
    requires_attunement = True


class SpearOfLightning(MagicItem):
    """When you hurl it and speak its Command Word, it transforms into a bolt of
    lightning, forming a line 5 feet wide that extends out from you to a target
    within 120 feet. Each creature in the line excluding you and the target
    must make a DC 13 Dexterity saving throw, taking 4d6 lightning damage on a
    failed save, and half as much damage on a successful one. The Lightning
    Bolt turns back into a spear when it reaches the target.

    Make a ranged weapon Attack against the target. On a hit, the target takes
    damage from the spear plus 4d6 lightning damage.

    The spear's property can't be used again until the next dawn. In the
    meantime, the spear can still be used as a Magic Weapon.
    """
    requires_attunement = True
    name = "Lightning Spear"


class MaulOfRetaliation(MagicItem):
    """
    While you hold this maul and it is attuned to you, you can use a reaction to
    make a single melee attack with it against any creature within reach that deals
    damage to you. You have advantage on the attack roll, and any damage dealt
    with this attack ignores any damage immunity or resistance the target has.
    """
    requires_attunement = True
    name = "Maul of Retaliation"


class AmuletOfTheEel(MagicItem):
    """While holding this amulet, you can breath water and air, and have a
    swimming speed of 20'."""
    name = "Amulet of the Eel"
    

class BracersOfMagnetism(MagicItem):
    """When wearing these bracers, you can use a bonus action to speak their
    command word, causing them to become magnetically attractive to each other.

    While active, the wearer's arms are secured together, requiring a succesful DC 25 
    STR (Athletics) check to separate them by six inches. The wearer has advantage 
    on all STR (Athletics) checks made to grapple, but disadvantage on all
    weapon attacks and DEX (Sleight of Hand) checks. 

    The wearer can use another bonus action to speak the command word and 
    deactivate the magnetic effect.

    The magnetic effect fails if the bracers are more than 10' apart.
    """
    requires_attunement = True
    name = "Bracers of Magnetism"


class ShieldOfFaces(MagicItem):
    """This +1 metallic shield has a detailed face chisled into its front surface.
    As a bonus action, the wielder can use a bonus action to mentally command
    the shield to adopt a new emotional state (such as "smiling", "laughing",
    "crying", etc.)

    """
    requires_attunement = True
    name = "Shield of Faces"


class GlowingSword(MagicItem):
    """
    This strange longsword glows at odd times.
    """
    name = "Glowing Sword"


class EagleWhistle(MagicItem):
    """
    While you blow an eagle whistle continuously, you can fly
    twice as fast as your walking speed. You can blow the whistle continuously
    for a number of rounds equal to 5 plus five times your CON modifier
    (minimum of one round) or until you talk, hold your breath, or start
    suffocating. A use of the whistle also ends if you land. If you are aloft
    when you stop blowing the whistle, you fall. The whistle has three uses.
    It regains expended uses daily at dawn.
    """
    name = "Eagle Whistle"


class RingOfColdResistance(MagicItem):
    """
    You have Resistance to cold damage while wearing this ring.

    """
    name = "Ring of Cold Protection"
    requires_attunement = True


class RobeOfStars(MagicItem):
    """This black or dark blue robe is embroidered with small white or silver
    stars. You gain a +1 bonus to Saving Throws while you wear it.

    Six stars, located on the robe's upper front portion, are particularly
    large. While wearing this robe, you can use an action to pull off one of
    the stars and use it to cast Magic Missile as a 5th-level spell. Daily at
    dusk, 1d6 removed stars reappear on the robe.

    While you wear the robe, you can use an action to enter the Astral Plane
    along with everything you are wearing and carrying. You remain there until
    you use an action to return to the plane you were on. You reappear in the
    last space you occupied, or if that space is occupied, the nearest
    unoccupied space.

    """
    name = "Robe of Stars"
    requires_attunement = True
    saving_throw_bonus = 1


class MedalionOfThoughts(MagicItem):
    """
    The medallion has 3 Charges. While wearing it, you can use an action and
    expend 1 charge to cast the Detect Thoughts spell (save DC 13) from it. The
    medallion regains 1d3 expended Charges daily at dawn.

    """
    name = "Medalion of Thoughts"

    
class SlippersOfSpiderClimbing(MagicItem):
    """
    While you wear these light shoes, you can move up, down, and across
    vertical surfaces and upside down along ceilings, while leaving your hands
    free. You have a climbing speed equal to your walking speed. However, the
    slippers don't allow you to move this way on a slippery surface, such as
    one covered by ice or oil.

    """
    name = "Slippers of Spider Climbing"


class OilOfSharpness(MagicItem):
    """This clear, gelatinous oil sparkles with tiny, ultrathin silver shards. The
    oil can coat one slashing or piercing weapon or up to 5 pieces of slashing
    or piercing Ammunition. Applying the oil takes 1 minute. For 1 hour, the
    coated item is magical and has a +3 bonus to Attack and Damage Rolls.
    """
    name = "Oil of Sharpness"
    
    
class BracersOfDefense(MagicItem):
    """


    """
    name = "Bracers of Defense"
    ac_bonus = 2
    rarity = "Rare"


class OrbOfTime(MagicItem):
    """While holding this orb, you can use an action to determine whether it is
    morning, afternoon, evening, or nighttime outside. This property functions
    only on the Material Plane.

    """
    name = "Orb of Time"


class GlovesOfThievery(MagicItem):
    """These gloves are invisible while worn. While wearing them, you gain a +5
    bonus to Dexterity (Sleight of Hand checks and Dexterity checks made to
    pick locks.

    """
    name = "Gloves of Thievery"
    other_bonuses = {'sleight of hand': 5, }


class BootsOfTheWinterlands(MagicItem):
    """These furred boots are snug and feel quite warm. While you wear them, you
    gain the following benefits:

    - You have Resistance to cold damage.

    - You ignore difficult terrain created by ice or snow.

    - You can tolerate temperatures as low as -50 degrees Fahrenheit without
      any additional Protection. If you wear heavy clothes, you can tolerate
      temperatures as low as -100 degrees Fahrenheit.

    """
    name = "Boots of the Winterlands"
    requires_attunement = True


class BagOfRustColoredTricks(MagicItem):
    """This ordinary bag, made from gray, rust, or tan cloth, appears
    empty. Reaching inside the bag, however, reveals the presence of a small,
    fuzzy object. The bag weighs 1/2 pound.  You can use an action to pull the
    fuzzy object from the bag and throw it up to 20 feet. When the object
    lands, it transforms into a creature you determine by rolling a d8 and
    consulting the table that corresponds to the bag's color. The creature
    vanishes at the next dawn or when it is reduced to 0 Hit Points.  The
    creature is friendly to you and your companions, and it acts on Your
    Turn. You can use a Bonus Action to Command how the creature moves and what
    action it takes on its next turn, or to give it general orders, such as to
    Attack your enemies. In the absence of such orders, the creature acts in a
    fashion appropriate to its Nature.  Once three fuzzy Objects have been
    pulled from the bag, the bag can't be used again until the next dawn.

    Rust Colored:
    
    1 - Rat
    
    2 - Owl

    3 - Mastiff

    4 - Goat

    5 - Giant Goat

    6 - Giant Boar

    7 - Lion

    8 - Brown Bear
    """
    name = "Bag of Tricks"


class BagOfHolding(MagicItem):
    """This bag has an interior space considerably larger than its outside
    dimensions, roughly 2 feet in diameter at the mouth and 4 feet deep. The
    bag can hold up to 500 pounds, not exceeding a volume of 64 cubic feet. The
    bag weighs 15 pounds, regardless of its contents. Retrieving an item from
    the bag requires an action.

    If the bag is overloaded, pierced, or torn, it ruptures and is destroyed,
    and its contents are scattered in the Astral Plane. If the bag is turned
    inside out, its contents spill forth, unharmed, but the bag must be put
    right before it can be used again. Breathing creatures inside the bag can
    survive up to a number of minutes equal to 10 divided by the number of
    creatures (minimum 1 minute), after which time they begin to suffocate.

    Placing a bag of holding inside an extradimensional space created by a
    Handy Haversack, Portable Hole, or similar item instantly destroys both
    items and opens a gate to the Astral Plane. The gate originates where the
    one item was placed inside the other. Any creature within 10 feet of the
    gate is sucked through it to a random location on the Astral Plane. The
    gate then closes. The gate is one-way only and can't be reopened.

    """
    name = "Bag of Holding"


class StoneOfGoodLuck(MagicItem):
    """While this polished agate is on your person, you gain a +1 bonus to Ability
    Checks and Saving Throws.

    """
    name = "Stone of Good Luck"
    saving_throw_bonus = 1
    skill_check_bonus = 1


