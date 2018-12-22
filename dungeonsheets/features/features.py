from .. import weapons


def create_feature(**params):
    """Create a new subclass of ``Feature`` with given default parameters.
    
    Useful for features that haven't been entered into the ``features.py``
    file yet.
    
    Parameters
    ----------
    params : optional
      Saved as attributes of the new class.
    
    Returns
    -------
    NewFeature
      New feature class, subclass of ``Feature``, with given params.
    """
    NewFeature = type('UnknownFeature', (Feature,), params)
    return NewFeature


class Feature():
    """
    Provide full text of rules in documentation
    """
    name = "Generic Feature"
    source = ''  # race, class, background, etc.
    spells_known = ()
    spells_prepared = ()
    needs_implementation = False  # Set to True if need to find way to compute stats

    def __eq__(self, other):
        return (self.name == other.name) and (self.source == other.source)

    def __hash__(self):
        return 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)
    
    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        Updates weapon based on the Feature property

        Parameters
        ----------
        weapon
           The weapon to be tested for special bonuses
        kwargs
           Any other key-word arguments the function may require

        Returns
        -------
        weapon
            Updated weapon (perhaps changed damage bonus, etc.)

        """
        return weapon

    def AC_func(self, char, **kwargs):
        """
        Return the alternative AC from having this feat

        The character will take max AC from all available feats / standard AC,
        so the default is to output very low AC

        Parameters
        ----------
        char
           Character object, to check for necessary abilities, etc.
        kwargs
           Any other key-word arguments the function may require

        Returns
        -------
        AC : integer armor class from this feature
        """
        return -100


class FeatureSelector(Feature):
    """
    A feature with multiple possible choices.
    """
    options = dict()

    def __init__(self, feature_choices=[]):
        keep_source = self.source
        # Look for matching feature_choices
        for selection in feature_choices:
            if selection.lower() in self.options():
                new_feat = self.options[selection.lower()]
                self.__dict__.update(new_feat.__dict__)
                new_feat.__init__(self)
                break
        self.source = keep_source