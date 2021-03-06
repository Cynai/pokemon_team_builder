from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

# Create your models here.

class UserProfile(models.Model):
    user = models.CharField(max_length=100, primary_key=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, default=None, null=True)
    friends = models.ManyToManyField('self')
    def __str__(self):
        return self.user.username

class Followlist(models.Model):
    follower = models.CharField(max_length=100)
    following = models.CharField(max_length=100)

class Like_Team(models.Model):
    user = models.CharField(max_length=100)
    teamname = models.CharField(max_length=30)

class Team(models.Model):
    userprofile = models.CharField(max_length=100)
    teamname = models.CharField(max_length=30, primary_key=True)
    likes = models.IntegerField(default=None, blank=True, null=True)
    slug = AutoSlugField(populate_from='teamname')

    # note - other tables hold data to be read so the user can
    # make selections and cannot hold this data for teams that
    # have already been submitted
    name1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    pokedex1 = models.IntegerField(default=None, blank=True, null=True)
    gmax1 = models.IntegerField(default=None, blank=True, null=True)
    type1_1 = models.CharField(max_length=10, default=None, blank=True, null=True)
    type2_1 = models.CharField(max_length=10, default=None, blank=True, null=True)
    ability1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    nature1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    item1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move1_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move2_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move3_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move4_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype1_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype2_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype3_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype4_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    level1 = models.IntegerField(default=None, blank=True, null=True)
    hp1 = models.IntegerField(default=None, blank=True, null=True)
    atk1 = models.IntegerField(default=None, blank=True, null=True)
    def1 = models.IntegerField(default=None, blank=True, null=True)
    sp_atk1 = models.IntegerField(default=None, blank=True, null=True)
    sp_def1 = models.IntegerField(default=None, blank=True, null=True)
    spd1 = models.IntegerField(default=None, blank=True, null=True)
    hpEV1 = models.IntegerField(default=None, blank=True, null=True)
    atkEV1 = models.IntegerField(default=None, blank=True, null=True)
    defEV1 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkEV1 = models.IntegerField(default=None, blank=True, null=True)
    sp_defEV1 = models.IntegerField(default=None, blank=True, null=True)
    spdEV1 = models.IntegerField(default=None, blank=True, null=True)
    hpIV1 = models.IntegerField(default=None, blank=True, null=True)
    atkIV1 = models.IntegerField(default=None, blank=True, null=True)
    defIV1 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkIV1 = models.IntegerField(default=None, blank=True, null=True)
    sp_defIV1 = models.IntegerField(default=None, blank=True, null=True)
    spdIV1 = models.IntegerField(default=None, blank=True, null=True)

    name2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    pokedex2 = models.IntegerField(default=None, blank=True, null=True)
    gmax2 = models.IntegerField(default=None, blank=True, null=True)
    type1_2 = models.CharField(max_length=10, default=None, blank=True, null=True)
    type2_2 = models.CharField(max_length=10, default=None, blank=True, null=True)
    ability2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    nature2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    item2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move1_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move2_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move3_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move4_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype1_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype2_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype3_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype4_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    level2 = models.IntegerField(default=None, blank=True, null=True)
    hp2 = models.IntegerField(default=None, blank=True, null=True)
    atk2 = models.IntegerField(default=None, blank=True, null=True)
    def2 = models.IntegerField(default=None, blank=True, null=True)
    sp_atk2 = models.IntegerField(default=None, blank=True, null=True)
    sp_def2 = models.IntegerField(default=None, blank=True, null=True)
    spd2 = models.IntegerField(default=None, blank=True, null=True)
    hpEV2 = models.IntegerField(default=None, blank=True, null=True)
    atkEV2 = models.IntegerField(default=None, blank=True, null=True)
    defEV2 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkEV2 = models.IntegerField(default=None, blank=True, null=True)
    sp_defEV2 = models.IntegerField(default=None, blank=True, null=True)
    spdEV2 = models.IntegerField(default=None, blank=True, null=True)
    hpIV2 = models.IntegerField(default=None, blank=True, null=True)
    atkIV2 = models.IntegerField(default=None, blank=True, null=True)
    defIV2 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkIV2 = models.IntegerField(default=None, blank=True, null=True)
    sp_defIV2 = models.IntegerField(default=None, blank=True, null=True)
    spdIV2 = models.IntegerField(default=None, blank=True, null=True)

    name3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    pokedex3 = models.IntegerField(default=None, blank=True, null=True)
    gmax3 = models.IntegerField(default=None, blank=True, null=True)
    type1_3 = models.CharField(max_length=10, default=None, blank=True, null=True)
    type2_3 = models.CharField(max_length=10, default=None, blank=True, null=True)
    ability3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    nature3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    item3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move1_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move2_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move3_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move4_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype1_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype2_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype3_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype4_3 = models.CharField(max_length=100, default=None, blank=True, null=True)
    level3 = models.IntegerField(default=None, blank=True, null=True)
    hp3 = models.IntegerField(default=None, blank=True, null=True)
    atk3 = models.IntegerField(default=None, blank=True, null=True)
    def3 = models.IntegerField(default=None, blank=True, null=True)
    sp_atk3 = models.IntegerField(default=None, blank=True, null=True)
    sp_def3 = models.IntegerField(default=None, blank=True, null=True)
    spd3 = models.IntegerField(default=None, blank=True, null=True)
    hpEV3 = models.IntegerField(default=None, blank=True, null=True)
    atkEV3 = models.IntegerField(default=None, blank=True, null=True)
    defEV3 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkEV3 = models.IntegerField(default=None, blank=True, null=True)
    sp_defEV3 = models.IntegerField(default=None, blank=True, null=True)
    spdEV3 = models.IntegerField(default=None, blank=True, null=True)
    hpIV3 = models.IntegerField(default=None, blank=True, null=True)
    atkIV3 = models.IntegerField(default=None, blank=True, null=True)
    defIV3 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkIV3 = models.IntegerField(default=None, blank=True, null=True)
    sp_defIV3 = models.IntegerField(default=None, blank=True, null=True)
    spdIV3 = models.IntegerField(default=None, blank=True, null=True)

    name4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    pokedex4 = models.IntegerField(default=None, blank=True, null=True)
    gmax4 = models.IntegerField(default=None, blank=True, null=True)
    type1_4 = models.CharField(max_length=10, default=None, blank=True, null=True)
    type2_4 = models.CharField(max_length=10, default=None, blank=True, null=True)
    ability4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    nature4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    item4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move1_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move2_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move3_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move4_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype1_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype2_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype3_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype4_4 = models.CharField(max_length=100, default=None, blank=True, null=True)
    level4 = models.IntegerField(default=None, blank=True, null=True)
    hp4 = models.IntegerField(default=None, blank=True, null=True)
    atk4 = models.IntegerField(default=None, blank=True, null=True)
    def4 = models.IntegerField(default=None, blank=True, null=True)
    sp_atk4 = models.IntegerField(default=None, blank=True, null=True)
    sp_def4 = models.IntegerField(default=None, blank=True, null=True)
    spd4 = models.IntegerField(default=None, blank=True, null=True)
    hpEV4 = models.IntegerField(default=None, blank=True, null=True)
    atkEV4 = models.IntegerField(default=None, blank=True, null=True)
    defEV4 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkEV4 = models.IntegerField(default=None, blank=True, null=True)
    sp_defEV4 = models.IntegerField(default=None, blank=True, null=True)
    spdEV4 = models.IntegerField(default=None, blank=True, null=True)
    hpIV4 = models.IntegerField(default=None, blank=True, null=True)
    atkIV4 = models.IntegerField(default=None, blank=True, null=True)
    defIV4 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkIV4 = models.IntegerField(default=None, blank=True, null=True)
    sp_defIV4 = models.IntegerField(default=None, blank=True, null=True)
    spdIV4 = models.IntegerField(default=None, blank=True, null=True)

    name5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    pokedex5 = models.IntegerField(default=None, blank=True, null=True)
    gmax5 = models.IntegerField(default=None, blank=True, null=True)
    type1_5 = models.CharField(max_length=10, default=None, blank=True, null=True)
    type2_5 = models.CharField(max_length=10, default=None, blank=True, null=True)
    ability5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    nature5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    item5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move1_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move2_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move3_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move4_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype1_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype2_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype3_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype4_5 = models.CharField(max_length=100, default=None, blank=True, null=True)
    level5 = models.IntegerField(default=None, blank=True, null=True)
    hp5 = models.IntegerField(default=None, blank=True, null=True)
    atk5 = models.IntegerField(default=None, blank=True, null=True)
    def5 = models.IntegerField(default=None, blank=True, null=True)
    sp_atk5 = models.IntegerField(default=None, blank=True, null=True)
    sp_def5 = models.IntegerField(default=None, blank=True, null=True)
    spd5 = models.IntegerField(default=None, blank=True, null=True)
    hpEV5 = models.IntegerField(default=None, blank=True, null=True)
    atkEV5 = models.IntegerField(default=None, blank=True, null=True)
    defEV5 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkEV5 = models.IntegerField(default=None, blank=True, null=True)
    sp_defEV5 = models.IntegerField(default=None, blank=True, null=True)
    spdEV5 = models.IntegerField(default=None, blank=True, null=True)
    hpIV5 = models.IntegerField(default=None, blank=True, null=True)
    atkIV5 = models.IntegerField(default=None, blank=True, null=True)
    defIV5 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkIV5 = models.IntegerField(default=None, blank=True, null=True)
    sp_defIV5 = models.IntegerField(default=None, blank=True, null=True)
    spdIV5 = models.IntegerField(default=None, blank=True, null=True)

    name6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    pokedex6 = models.IntegerField(default=None, blank=True, null=True)
    gmax6 = models.IntegerField(default=None, blank=True, null=True)
    type1_6 = models.CharField(max_length=10, default=None, blank=True, null=True)
    type2_6 = models.CharField(max_length=10, default=None, blank=True, null=True)
    ability6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    nature6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    item6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move1_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move2_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move3_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    move4_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype1_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype2_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype3_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    movetype4_6 = models.CharField(max_length=100, default=None, blank=True, null=True)
    level6 = models.IntegerField(default=None, blank=True, null=True)
    hp6 = models.IntegerField(default=None, blank=True, null=True)
    atk6 = models.IntegerField(default=None, blank=True, null=True)
    def6 = models.IntegerField(default=None, blank=True, null=True)
    sp_atk6 = models.IntegerField(default=None, blank=True, null=True)
    sp_def6 = models.IntegerField(default=None, blank=True, null=True)
    spd6 = models.IntegerField(default=None, blank=True, null=True)
    hpEV6 = models.IntegerField(default=None, blank=True, null=True)
    atkEV6 = models.IntegerField(default=None, blank=True, null=True)
    defEV6 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkEV6 = models.IntegerField(default=None, blank=True, null=True)
    sp_defEV6 = models.IntegerField(default=None, blank=True, null=True)
    spdEV6 = models.IntegerField(default=None, blank=True, null=True)
    hpIV6 = models.IntegerField(default=None, blank=True, null=True)
    atkIV6 = models.IntegerField(default=None, blank=True, null=True)
    defIV6 = models.IntegerField(default=None, blank=True, null=True)
    sp_atkIV6 = models.IntegerField(default=None, blank=True, null=True)
    sp_defIV6 = models.IntegerField(default=None, blank=True, null=True)
    spdIV6 = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = "team_table"

    def __str__(self):
        return self.teamname

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if self.likes < 0:
            self.likes = 0

        self.slug = slugify(self.teamname)
        super(Team, self).save(*args, **kwargs)

class Pokemon(models.Model):
    pokedex = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    type1 = models.CharField(max_length=10, default=None)
    type2 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pokedex < 0:
            self.pokedex = None
        self.slug = slugify(self.name)
        super(Pokemon, self).save(*args, **kwargs)

class Move(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)

    #fields not needed without damage calculator
    #pp = models.IntegerField()
    #power = models.IntegerField()
    #accuracy = models.IntegerField()

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Nature(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    upstat = models.CharField(max_length=10, default=None, blank=True, null=True)
    downstat = models.CharField(max_length=10, default=None, blank=True, null=True)