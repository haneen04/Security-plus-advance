from django.db import models

class FacesLogs(models.Model):
    facecnic = models.CharField(db_column='FaceCNIC', max_length=20)  # Field name made lowercase.
    detect_time = models.DateTimeField(db_column='Detect_Time')  # Field name made lowercase.
    detect_camera_id = models.CharField(db_column='Detect_Camera_ID', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'Faces_logs'

class Add_Profile (models.Model):
    pernme = models.CharField(db_column='PerNme', max_length=50, null=False)  # Field name made lowercase.
    percnic = models.CharField(db_column='PerCNIC',max_length=16)  # Field name made lowercase.
    perrnk = models.CharField(db_column='PerRnk', max_length=30, blank=True, null=True)  # Field name made lowercase.
    perposition = models.CharField(db_column='PerPosition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    perroomno = models.CharField(db_column='PerRoomNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    perwrkhr = models.CharField(db_column='PerWrkHr', max_length=10, blank=True, null=True)  # Field name made lowercase.
    perwrkdys = models.CharField(db_column='PerWrkDys', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pertype = models.CharField(db_column='PerType', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Perprofile'

class FaceImages (models.Model): 

    facecnic = models.CharField(db_column='FaceCNIC',max_length=16)  # Field name made lowercase.    
    faceimgpath1 = models.ImageField(db_column='FaceImgPath1', blank=True, null=True, upload_to="images/" )  # Field name made lowercase.
    faceimgpath2 = models.ImageField(db_column='FaceImgPath2', blank=True, null=True, upload_to="images/")  # Field name made lowercase.
    faceimgpath3 = models.ImageField(db_column='FaceImgPath3', blank=True, null=True, upload_to="images/")  # Field name made lowercase.
    faceimgpath4 = models.ImageField(db_column='FaceImgPath4', blank=True, null=True, upload_to="images/")  # Field name made lowercase.
    faceimgpath5 = models.ImageField(db_column='FaceImgPath5', blank=True, null=True, upload_to="images/")  # Field name made lowercase.
    faceimgpath6 = models.ImageField(db_column='FaceImgPath6', blank=True, null=True, upload_to="images/")  # Field name made lowercase.
    faceimgpath7 = models.ImageField(db_column='FaceImgPath7', blank=True, null=True, upload_to="images/")  # Field name made lowercase.
    faceimgpath8 = models.ImageField(db_column='FaceImgPath8', blank=True, null=True, upload_to="images/")  # Field name made lowercase.


    class Meta:
        db_table = 'FaceImages'


class Cameras(models.Model):
    camid = models.CharField(db_column='CamID', max_length=50)  # Field name made lowercase.
    camip = models.CharField(db_column='CamIP', max_length=50)  # Field name made lowercase.
    camloc = models.CharField(db_column='CamLoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cammotion = models.CharField(db_column='CamMotion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    camdetect = models.CharField(db_column='CamDetect', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cammegpixl = models.CharField(db_column='camMegPixl', max_length=5, blank=True, null=True)
    camzoomsize = models.CharField(db_column='camZoomSize', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'Cameras'   