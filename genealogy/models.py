# 
# Based on Gramps model.py
#

from django.db import models

#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic
#from gramps.gen.lib.date import Date as GDate, Today
#from gramps.gen.utils.id import create_id, create_uid
#from gramps.webapp.grampsdb.profile import Profile

#---------------------------------------------------------------------------
#
# Types
#
#---------------------------------------------------------------------------

NAME_TYPE = ((0, 'Unknown'),
             (0, 'Custom'),
             (1, 'Also Known As'),
             (2, 'Birth Name'),
             (3, 'Married Name'),
)

NAME_ORIGIN_TYPE = ((1, ''),
                    (0, 'Custom'),
                    (7, 'Feudal'),
                    (3, 'Given'),
                    (2, 'Inherited'),
                    (12, 'Location'),
                    (10, 'Matrilineal'),
                    (6, 'Matronymic'),
                    (11, 'Occupation'),
                    (9, 'Patrilineal'),
                    (5, 'Patronymic'),
                    (8, 'Pseudonym'),
                    (4, 'Taken'),
                    (-1, 'Unknown'),
)

ATTRIBUTE_TYPE = ((-1, 'Unknown'),
                  (0, 'Custom'),
                  (1, 'Caste'),
                  (2, 'Description'),
                  (3, 'Identification Number'),
                  (4, 'National Origin'),
                  (5, 'Number of Children'),
                  (6, 'Social Security Number'),
                  (7, 'Nickname'),
                  (8, 'Cause'),
                  (9, 'Agency'),
                  (10, 'Age'),
                  (11, 'Father Age'),
                  (12, 'Mother Age'),
                  (13, 'Witness'),
                  (14, 'Time'),
)
    
URL_TYPE = ((-1, 'Unknown'),
            (0, 'Custom'),
            (1, 'E-mail'),
            (2, 'Web Home'),
            (3, 'Web Search'),
            (4, 'FTP'),
)    

CHILD_REF_TYPE = ((0, 'None'),
                  (1, 'Birth'),
                  (2, 'Adopted'),
                  (3, 'Stepchild'),
                  (4, 'Sponsored'),
                  (5, 'Foster'),
                  (6, 'Unknown'),
                  (7, 'Custom'),
)

REPOSITORY_TYPE = ((-1, 'Unknown'),
                   (0, 'Custom'),
                   (1, 'Library'),
                   (2, 'Cemetery'),
                   (3, 'Church'),
                   (4, 'Archive'),
                   (5, 'Album'),
                   (6, 'Web site'),
                   (7, 'Bookstore'),
                   (8, 'Collection'),
                   (9, 'Safe'),
)

EVENT_TYPE = ((-1, 'Unknown'),
              (0, 'Custom'),
              (1, 'Marriage'),
              (2, 'Marriage Settlement'),
              (3, 'Marriage License'),
              (4, 'Marriage Contract'),
              (5, 'Marriage Banns'),
              (6, 'Engagement'),
              (7, 'Divorce'),
              (8, 'Divorce Filing'),
              (9, 'Annulment'),
              (10, 'Alternate Marriage'),
              (11, 'Adopted'),
              (12, 'Birth'),
              (13, 'Death'),
              (14, 'Adult Christening'),
              (15, 'Baptism'),
              (16, 'Bar Mitzvah'),
              (17, 'Bas Mitzvah'),
              (18, 'Blessing'),
              (19, 'Burial'),
              (20, 'Cause Of Death'),
              (21, 'Census'),
              (22, 'Christening'),
              (23, 'Confirmation'),
              (24, 'Cremation'),
              (25, 'Degree'),
              (26, 'Education'),
              (27, 'Elected'),
              (28, 'Emigration'),
              (29, 'First Communion'),
              (30, 'Immigration'),
              (31, 'Graduation'),
              (32, 'Medical Information'),
              (33, 'Military Service'),
              (34, 'Naturalization'),
              (35, 'Nobility Title'),
              (36, 'Number of Marriages'),
              (37, 'Occupation'),
              (38, 'Ordination'),
              (39, 'Probate'),
              (40, 'Property'),
              (41, 'Religion'),
              (42, 'Residence'),
              (43, 'Retirement'),
              (44, 'Will'),
)

FAMILY_REL_TYPE = ((3, 'Unknown'),
                   (4, 'Custom'),
                   (2, 'Civil Union'),
                   (1, 'Unmarried'),
                   (0, 'Married'),
)

SOURCE_MEDIA_TYPE=((-1, 'Unknown'),
                   (0, 'Custom'),
                   (1, 'Audio'),
                   (2, 'Book'),
                   (3, 'Card'),
                   (4, 'Electronic'),
                   (5, 'Fiche'),
                   (6, 'Film'),
                   (7, 'Magazine'),
                   (8, 'Manuscript'),
                   (9, 'Map'),
                   (10, 'Newspaper'),
                   (11, 'Photo'),
                   (13, 'Tombstone'),
                   (13, 'Video'),
)

EVENT_ROLE_TYPE=((-1, 'Unknown'), 
                 (0, 'Custom'),
                 (1, 'Primary'),
                 (2, 'Clergy'),
                 (3, 'Celebrant'),
                 (4, 'Aide'),
                 (5, 'Bride'),
                 (6, 'Groom'),
                 (7, 'Witness'),
                 (8, 'Family'),
                 (9, 'Informant'),
)

NOTE_TYPE = ((-1, 'Unknown'),
             (0, 'Custom'),
             (1, 'General'),
             (2, 'Research'),
             (3, 'Transcript'),
             (4, 'Person Note'),
             (5, 'Attribute Note'),
             (6, 'Address Note'),
             (7, 'Association Note'),
             (8, 'LDS Note'),
             (9, 'Family Note'),
             (10, 'Event Note'),
             (11, 'Event Reference Note'),
             (12, 'Source Note'),
             (13, 'Source Reference Note'),
             (14, 'Place Note'),
             (15, 'Repository Note'),
             (16, 'Repository Reference Note'),
             (17, 'Media Note'),
             (18, 'Media Reference Note'),
             (19, 'Child Reference Note'),
             (20, 'Name Note'),
             (21, 'Source text'),
             (22, 'Citation'),
             (23, 'Report'),
             (24, 'Html code'),
)

GENDER_TYPE = ((2, 'Unknown'), 
               (1, 'Male'), 
               (0, 'Female'), 
)

LDS_TYPE = ((0, "Baptism"),
                (1, "Endowment"),
                (2, "Seal to Parents"),
                (3, "Seal to Spouse"),
                (4, "Confirmation")
)

LDS_STATUS = ((0, "None"),
                (1, "BIC"), 
                (2, "Canceled"),
                (3, "Child"),
                (4, "Cleared"),
                (5, "Completed"),
                (6, "Dns"),
                (7, "Infant"),
                (8, "Pre 1970"),
                (9, "Qualified"),
                (10, "DNSCAN"),
                (11, "Stillborn"),
                (12, "Submitted"),
                (13, "Uncleared")
)

NAME_FORMAT_TYPE = ((0, "Default format"),
                (1, "Surname, Given Patronymic"),
                (2, "Given Surname"),
                (3, "Patronymic, Given"),
)

CALENDAR_TYPE = ((0, "Gregorian"),
                (1, "Julian"),
                (2, "Hebrew"),
                (3, "French Republican"),
                (4, "Persian"),
                (5, "Islamic"),
                (6, "Swedish")
)

DATE_NEW_YEAR_TYPE = ((0, ""),
                (1, "March 1"),
                (2, "March 25"),
                (3, "September 1"),
)

#---------------------------------------------------------------------------
#
# Support definitions
#
#---------------------------------------------------------------------------

class DateObject(models.Model):
    class Meta: abstract = True

    calendar = models.IntegerField(default=0)
    day1 = models.IntegerField(default=0)
    month1 = models.IntegerField(default=0)
    year1 = models.IntegerField(default=0)
    slash1 = models.BooleanField(default=False)
    day2 = models.IntegerField(blank=True, null=True)
    month2 = models.IntegerField(blank=True, null=True)
    year2 = models.IntegerField(blank=True, null=True)
    slash2 = models.NullBooleanField(blank=True, null=True)
    text = models.CharField(max_length=80, blank=True)
    sortval = models.IntegerField(default=0)
    newyear = models.IntegerField(default=0)

    def set_date_from_datetime(self, date_time, text=""):
        """
        Sets Date fields from an object that has year, month, and day
        properties.
        """
        y, m, d = date_time.year, date_time.month, date_time.day
        self.set_ymd(self, y, m, d, text=text)

    def set_date_from_ymd(self, y, m, d, text=""):
        """
        Sets Date fields from a year, month, and day.
        """
        gdate = GDate(y, m, d)
        gdate.text = text
        self.set_date_from_gdate(gdate)

    def set_date_from_gdate(self, gdate):
        """
        Sets Date fields from a Gramps date object.
        """
        (self.calendar, self.modifier, self.quality, dateval, self.text, 
         self.sortval, self.newyear) = gdate.serialize()
        if dateval is None:
            (self.day1, self.month1, self.year1, self.slash1) = 0, 0, 0, False
            (self.day2, self.month2, self.year2, self.slash2) = 0, 0, 0, False
        elif len(dateval) == 8:
            (self.day1, self.month1, self.year1, self.slash1, 
             self.day2, self.month2, self.year2, self.slash2) = dateval
        elif len(dateval) == 4:
            (self.day1, self.month1, self.year1, self.slash1) = dateval
            (self.day2, self.month2, self.year2, self.slash2) = 0, 0, 0, False

#---------------------------------------------------------------------------
#
# Primary Tables
#
#---------------------------------------------------------------------------
"""
class Tag(models.Model):
    handle = models.CharField(max_length=19, unique=True)
    gramps_id = models.TextField(blank=True, null=True)
    last_saved = models.DateTimeField('last changed', auto_now=True) 
    last_changed = models.DateTimeField('last changed', null=True,
                                        blank=True) # user edits
    last_changed_by = models.TextField(blank=True, null=True)

    name = models.TextField('name')
    color = models.CharField(max_length=13, blank=True, null=True) # "#000000000000" # Black
    priority = models.IntegerField('priority', blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def get_url(self):
        return "/tag/%s" % self.handle

    def get_link(self):
        return "<a href='%s'>%s</a>" % (self.get_url(), self.name)
"""

# Just the following have tag lists:
# ---------------------------------
#src/gen/lib/family.py
#src/gen/lib/mediaobj.py
#src/gen/lib/note.py
#src/gen/lib/person.py

class PrimaryObject(models.Model):
    """
    Common attribute of all primary objects with key on the handle
    """
    class Meta: abstract = True

    ## Fields:
    id = models.AutoField(primary_key=True)
    handle = models.CharField(max_length=19, unique=True)
    gramps_id =  models.CharField('ID', max_length=25, blank=True)

    private = models.BooleanField('private')
    public = models.BooleanField('public', default=True)

    def __unicode__(self): 
        return u"%s: %s" % (self.__class__.__name__,
                           self.gramps_id)

    def get_url(self):
        return "/%s-view/%s/" % (self.__class__.__name__.lower(),
                           self.handle)

class MyFamilies(models.Model):
    person = models.ForeignKey("Person")
    family = models.ForeignKey("Family")
    order = models.PositiveIntegerField(default=1)

#class MyParentFamilies(models.Model):
#    person = models.ForeignKey("Person")
#    family = models.ForeignKey("Family")
#    order = models.PositiveIntegerField(default=1)

class Person(PrimaryObject):
    """
    The model for the person object
    """
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    gender_type = models.IntegerField('GenderType', choices=GENDER_TYPE, default=2)
    
    probably_alive = models.BooleanField("Probably alive")
    
    events = models.ManyToManyField('Event', through="PersonEvent")
    birth = models.ForeignKey("Event", related_name="birth", blank=True, null=True)
    death = models.ForeignKey("Event", related_name="death", blank=True, null=True)
    
    families = models.ManyToManyField('Family', blank=True, null=True, through="MyFamilies")
    parent_family = models.ForeignKey('Family', related_name="parent_family", blank=True, null=True)
    
    
    
    #parent_families = models.ManyToManyField('Family', 
    #                                         related_name="parent_families",
    #                                         blank=True, null=True, 
    #                                         through='MyParentFamilies')
    
    
    #addresses = models.ManyToManyField('Address', null=True, blank=True)
#    references = generic.GenericRelation('PersonRef', related_name="refs",
#                                         content_type_field="object_type",
#                                         object_id_field="object_id")
    #tags = models.ManyToManyField('Tag', blank=True, null=True)

    def get_primary_name(self):
        """
        Return the preferred name of a person.
        """
        try:
            return u'%s %s' % (self.first_name, self.last_name) 
        except:
            return u""

    def __unicode__(self):
        return u"(%s [%s])" % (self.get_primary_name(), self.handle)

    def make_tag_list(self):
        return tuple()

    def get_selection_string(self):
        return self.name_set.get(preferred=True).get_selection_string()

class PersonEvent(models.Model):
    person = models.ForeignKey('Person')
    event = models.ForeignKey('Event')
    role = models.IntegerField(choices=EVENT_ROLE_TYPE, default=-1)

class Family(PrimaryObject):
    father = models.ForeignKey('Person', related_name="father_ref", 
                               null=True, blank=True)
    mother = models.ForeignKey('Person', related_name="mother_ref", 
                               null=True, blank=True)
    family_rel_type = models.IntegerField('FamilyRelType', choices=FAMILY_REL_TYPE, default=3)
    
    events = models.ManyToManyField('Event', through="FamilyEvent")
    marriage = models.ForeignKey("Event", related_name="marriage", blank=True, null=True)
    
    #tags = models.ManyToManyField('Tag', blank=True, null=True)
    
    #lds_list = models.ManyToManyField('Lds', null=True, blank=True)

    # Others keys here:
    #   .lds_set

    """
    def get_children(self):
        "
        Return all children from this family, in order."
        obj_type = ContentType.objects.get_for_model(self)
        childrefs = ChildRef.objects.filter(object_id=self.id,
                                            object_type=obj_type).order_by("order")
        return [childref.ref_object for childref in childrefs]
    """

    def __unicode__(self):
        father = self.father.get_primary_name() if self.father else "No father"
        mother = self.mother.get_primary_name() if self.mother else "No mother"
        return u"(%s and %s [%s])" % (father, mother, self.handle)

    # Other keys here:
    #   .datamap_set

class FamilyEvent(models.Model):
    family = models.ForeignKey('Family')
    event = models.ForeignKey('Event')
    role = models.IntegerField(choices=EVENT_ROLE_TYPE, default=-1)

class Event(DateObject, PrimaryObject):
    event_type = models.IntegerField('EventType', choices=EVENT_TYPE)
    description = models.TextField('description', blank=True)
    place = models.ForeignKey('Place', null=True, blank=True)
#    references = generic.GenericRelation('EventRef', related_name="refs",
#                                         content_type_field="object_type",
#                                         object_id_field="object_id")
    
    def __unicode__(self):
        return "[%s] (%s) %s" % (self.gramps_id, 
                                 self.event_type, 
                                 self.description)

class Place(PrimaryObject):
    title = models.TextField(blank=True)
    #locations = models.ManyToManyField('Location', null=True, blank=True)
    long = models.TextField(blank=True)
    lat = models.TextField(blank=True)
    #url_list = models.ManyToManyField('Url', null=True, blank=True)

    def get_selection_string(self):
        return "%s [%s]" % (self.title, self.gramps_id)

    def __unicode__(self):
        return str(self.title)

    # Others keys here:
    #   .url_set
    #   .location_set

class Media(DateObject, PrimaryObject):
    path = models.TextField(blank=True)
    mime = models.TextField(blank=True, null=True)
    desc = models.TextField("Title", blank=True)
#    references = generic.GenericRelation('MediaRef', related_name="refs",
#                                         content_type_field="object_type",
#                                         object_id_field="object_id")
    #tags = models.ManyToManyField('Tag', blank=True, null=True)

    def make_tag_list(self):
        return tuple()

    def __unicode__(self):
        return str(self.desc)

class Note(PrimaryObject):
    note_type = models.IntegerField('NoteType', choices=NOTE_TYPE)
    text  = models.TextField(blank=True)
    preformatted = models.BooleanField('preformatted')
#    references = generic.GenericRelation('NoteRef', related_name="refs",
#                                         content_type_field="object_type",
#                                         object_id_field="object_id")
    #tags = models.ManyToManyField('Tag', blank=True, null=True)

    def make_tag_list(self):
        return tuple()

    def __unicode__(self):
        return str(self.gramps_id)
