from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


class OathOfDevotion(SubClass):
    """The Oath of Devotion binds a paladin to the loftiest ideals of justice,
    virtue, and order. Sometim es called cavaliers, white knights, or holy
    warriors, these paladins meet the ideal of the knight in shining armor,
    acting with honor in pursuit o f justice and the greater good. They hold
    themselves to the highest standards of conduct, and some, for better or
    worse, hold the rest of the world to the same standards. Many who swear
    this oath are devoted to gods of law and good and use their gods’ tenets as
    the measure o f their devotion. They hold angels—the perfect servants o f
    good—as their ideals, and incorporate images of angelic wings into their
    helmets or coats of arms.

    **Tenets of Devotion**: Though the exact words and strictures of the Oath
    of Devotion vary, paladins of this oath share these tenets.

    --Honesty. Don’t lie or cheat. Let your word be your promise.

    --Courage. Never fear to act, though caution is wise.

    --Compassion. Aid others, protect the weak, and punish those who threaten
    them. Show mercy to your foes, but temper it with wisdom.

    --Honor. Treat others with fairness, and let your honorable deeds be an
    example to them. Do as much good as possible while causing the least amount
    of harm.

    --Duty. Be responsible for your actions and their consequences, protect
    those entrusted to your care, and obey those who have just authority over
    you.

    """
    name = "Oath of Devotion"
    features_by_level = defaultdict(list)
    
    
class OathOfAncients(SubClass):
    """The Oath of the Ancients is as old as the race of elves and the rituals of
    the druids. Sometimes called fey knights, green knights, or horned knights,
    paladins who swear this oath cast their lot with the side of the light in
    the cosm ic struggle against darkness because they love the beautiful and
    life-giving things of the world, not necessarily because they believe in
    principles of honor, courage, and justice. They adorn their armor and
    clothing with images of growing things—leaves, antlers, or flowers—to
    reflect their commitment to preserving life and light in the world. 

    **Tenets of the Ancients**: The tenets of the Oath of the Ancients have
      been preserved for uncounted centuries. This oath emphasizes the
      principles of good above any concerns of law or chaos. Its four central
      principles are simple.

    --Kindle the Light. Through your acts of mercy, kindness, and forgiveness,
    kindle the light of hope in the world, beating back despair.

    --Shelter the Light. Where there is good, beauty, love, and laughter in the
    world, stand against the w ickedness that would swallow it. Where life
    flourishes, stand against the forces that would render it barren.

    --Preserve Your Own Light. Delight in song and laughter, in beauty and
    art. If you allow the light to die in your own heart, you can’t preserve it
    in the world.

    --Be the Light. Be a glorious beacon for all who live in despair. Let the
    light of your joy and courage shine forth in all your deeds.

    """
    name = "Oath of The Ancients"
    features_by_level = defaultdict(list)
    
    
class OathOfVengance(SubClass):
    """The Oath of Vengeance is a solemn commitment to punish those who have
    committed a grievous sin. When evil forces slaughter helpless villagers,
    when an entire people turns against the will of the gods, when a thieves’
    guild grows too violent and powerful, when a dragon rampages through the
    countryside—at times like these, paladins arise and swear an Oath of
    Vengeance to set right that which has gone wrong. To these paladins—
    sometimes called avengers or dark knights—their own purity is not as
    important as delivering justice.

    **Tenets of Vengance**: The tenets of the Oath of Vengeance vary by
    paladin, but all the tenets revolve around punishing wrongdoers by any
    means necessary. Paladins who uphold these tenets are willing to sacrifice
    even their own righteousness to mete out justice upon those who do evil, so
    the paladins are often neutral or lawful neutral in alignment. The core
    principles of the tenets are brutally simple.

    --Fight the Greater Evil. Faced with a choice of fighting my sworn foes or
    combating a lesser evil. I choose the greater evil.

    --No Mercy for the Wicked. Ordinary foes might win my mercy, but my sworn
    enemies do not.

    --By Any Means Necessary. My qualms can’t get in the way of exterminating
    my foes.

    --Restitution. If my foes wreak ruin on the world, it is because I failed
    to stop them. I must help those harmed by their misdeeds.

    """
    name = "Oath of Vengance"
    features_by_level = defaultdict(list)
    
    
class OathOfCrown(SubClass):
    """The Oath of the Crown is sworn to the ideals of civilization, be it the
    spirit of a nation, fealty to a sovereign, or service to a deity of law and
    rulership. The paladins who swear this oath dedicate themselves to serving
    society and, in particular, the just laws that hold society together. These
    paladins are the watchful guardians on the walls, standing against the
    chaotic tides of barbarism that threaten to tear down all that
    civilization has built, and are commonly known as guardians, exemplars,
    or sentinels. Often, paladins who swear this oath are members of an order
    of knighthood in service to a nation or a sovereign, and undergo their oath
    as part of their admission to the order's ranks.

    **Tenets of the Crown**: The tenets of the Oath of the Crown are often set
    by the sovereign to which their oath is sworn, but generally emphasize
    the following tenets.

    --Law. The law is paramount. It is the mortar that holds the stones of
    civilization together, and it must be respected.

    --Loyalty. Your word is your bond. Without loyalty, oaths and laws are
    meaningless.

    --Courage. You must be willing to do what needs to be done for the sake of
    order, even in the face of overwhelming odds. If you don't act, then who
    will?

    --Responsibility. You must deal with the consequences of your actions, and
    you are responsible for fulfilling your duties and obligations.

    """
    name = "Oath of The Crown"
    features_by_level = defaultdict(list)
    
    
class OathOfConquest(SubClass):
    """The Oath of Conquest calls to paladins who seek glory in battle and the
    subjugation of their enemies. It isn’t enough for these paladins to
    establish order. They must crush the forces of chaos. Sometimes called
    knight ty- rants or iron mongers, those who swear this oath gather into
    grim orders that serve gods or philosophies of war and well-ordered might.

    Some of these paladins go so far as to consort with the powers of the Nine
    Hells, valuing the rule of law over the balm of mercy. The archdevil Bel,
    warlord of Avernus, counts many of these paladins—called hell knights—as
    his most ardent supporters. Hell knights cover their armor with trophies
    taken from fallen en— emies, a grim~warning to any who dare oppose them and
    the decrees of their lords. These knights are often most fiercely resisted
    by other paladins of this oath, who believe that the hell knights have
    wandered too far into darkness.

    **Tenets of Conquest**: A paladin who takes this oath has the tenets of
    conquest seared on the upper arm.

    --Douse the Flame of Hope. It is not enough
    to merely defeat an enemy in battle. Your victory must be so over- whelming
    that your enemies' will to fight is shattered forever. A blade can end a
    life. Fear can end an empire.

    --Rule with an Iron Fist. Once you have conquered, tolerate no
    dissent. Your word is law. Those who obey it shall be favored. Those who
    defy it shall be punished as an example to all who might follow. 

    --Strength Above All. You shall rule until a stronger one arises. Then you
    must grow mightier and meet the challenge, or fall to your own ruin.

    """
    name = "Oath of Conquest"
    features_by_level = defaultdict(list)
    
    
class OathOfRedemption(SubClass):
    """The Oath of Redemption sets a paladin on a difficult path, one that requires
    a holy warrior to use violence only as a last resort. Paladins who dedicate
    themselves to this oath believe that any person can be redeemed and that
    the path of benevolence and justice is one that anyone can walk. These
    paladins face evil creatures in the hope of turning their foes to the
    light, and they slay their enemies only when such a deed will clearly save
    other lives. Paladins who follow this path are known as redeemers.

    While redeemers are idealists, they are no fools. Re— deemers know that
    undead, demons, devils, and other supernatural threats can be inherently
    evil. Against such fees, paladins who swear this oath bring the full wrath
    of their weapons and spells to bear. Yet the re- deemers still pray that,
    one day, even creatures of wick- edness will invite their own redemption.

    **Tenets of Redemption**: The tenets of the Oath of Redemption hold a
    paladin to a high standard of peace and justice.

    --Peace. Violence is a weapon of last resort. Diplomacy and understanding
    are the paths to long-lasting peace.

    --Innocence. All people begin life in an innocent state, and it is their
    environment or the influence of dark forces that drives them to evil. By
    setting the proper example, and working to heal the wounds of a deeply
    flawed world, you can set anyone on a righteous path.

    --Patience. Change takes time. Those who have walked the path of the wicked
    must be given reminders to keep them honest and true. Once you have planted
    the seed of righteousness in a creature, you must work day after day to
    allow that seed to survive and flourish.

    --Wisdom. Your heart and mind must stay clear, for eventually you will be
    forced to admit defeat. While ev- ery creature can be redeemed, some are so
    far along the path of evil that you have no choice but to end their lives
    for the greater good. Any such action must be carefully weighed and the
    consequences fully understood, but once you have made the decision, follow
    through with it knowing your path is just.

    """
    name = "Oath of Redemption"
    features_by_level = defaultdict(list)
    
    
class Paladin(CharClass):
    name = 'Paladin'
    hit_dice_faces = 10
    saving_throw_proficiencies = ('wisdom', 'charisma')
    _proficiencies_text = ('All armor', 'shields', 'simple weapons',
                           'martial weapons')
    weapon_proficiencies = weapons.simple_weapons + weapons.martial_weapons
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = ('light armor', 'medium armor', 'shields',
                                      'simple weapons', 'martial weapons')
    class_skill_choices = ("Athletics", 'Insight', 'Intimidation',
                           'Medicine', 'Persuasion', 'Religion')
    features_by_level = defaultdict(list)
    subclasses_available = (OathOfDevotion, OathOfAncients, OathOfVengance,
                            OathOfCrown, OathOfConquest, OathOfRedemption)
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        4:  (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5:  (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        6:  (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        7:  (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        8:  (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        9:  (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        10: (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        11: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        12: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        13: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        14: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        15: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        16: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        17: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        18: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        19: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        20: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    }