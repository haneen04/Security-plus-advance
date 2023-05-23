# Generated by Django 3.2.13 on 2023-05-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pernme', models.CharField(db_column='PerNme', max_length=50)),
                ('percnic', models.CharField(db_column='PerCNIC', max_length=16)),
                ('perrnk', models.CharField(blank=True, db_column='PerRnk', max_length=30, null=True)),
                ('perposition', models.CharField(blank=True, db_column='PerPosition', max_length=20, null=True)),
                ('perroomno', models.CharField(blank=True, db_column='PerRoomNo', max_length=20, null=True)),
                ('perwrkhr', models.CharField(blank=True, db_column='PerWrkHr', max_length=10, null=True)),
                ('perwrkdys', models.CharField(blank=True, db_column='PerWrkDys', max_length=10, null=True)),
                ('perimgpath', models.CharField(blank=True, db_column='PerImgPath', max_length=100, null=True)),
                ('pertype', models.CharField(blank=True, db_column='PerType', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Perprofile',
            },
        ),
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camid', models.CharField(db_column='CamID', max_length=50)),
                ('camip', models.CharField(db_column='CamIP', max_length=50)),
                ('camloc', models.CharField(blank=True, db_column='CamLoc', max_length=100, null=True)),
                ('cammotion', models.CharField(blank=True, db_column='CamMotion', max_length=20, null=True)),
                ('camdetect', models.CharField(blank=True, db_column='CamDetect', max_length=50, null=True)),
                ('cammegpixl', models.CharField(blank=True, db_column='camMegPixl', max_length=5, null=True)),
                ('camzoomsize', models.CharField(blank=True, db_column='camZoomSize', max_length=5, null=True)),
            ],
            options={
                'db_table': 'Cameras',
            },
        ),
        migrations.CreateModel(
            name='FaceImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True,serialize=False, verbose_name='ID')),
                ('facecnic', models.CharField(db_column='FaceCNIC', max_length=16)),
                ('faceimgpath1', models.CharField(blank=True, db_column='FaceImgPath1', max_length=100, null=True)),
                ('faceimgpath2', models.CharField(blank=True, db_column='FaceImgPath2', max_length=100, null=True)),
                ('faceimgpath3', models.CharField(blank=True, db_column='FaceImgPath3', max_length=100, null=True)),
                ('faceimgpath4', models.CharField(blank=True, db_column='FaceImgPath4', max_length=100, null=True)),
                ('faceimgpath5', models.CharField(blank=True, db_column='FaceImgPath5', max_length=100, null=True)),
                ('faceimgpath6', models.CharField(blank=True, db_column='FaceImgPath6', max_length=100, null=True)),
                ('faceimgpath7', models.CharField(blank=True, db_column='FaceImgPath7', max_length=100, null=True)),
                ('faceimgpath8', models.CharField(blank=True, db_column='FaceImgPath8', max_length=100, null=True)),
            ],
            options={
                'db_table': 'FaceImages',
            },
        ),
        migrations.CreateModel(
            name='FacesLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facecnic', models.CharField(db_column='FaceCNIC', max_length=20)),
                ('detect_time', models.DateTimeField(db_column='Detect_Time')),
                ('detect_camera_id', models.CharField(db_column='Detect_Camera_ID', max_length=20)),
            ],
            options={
                'db_table': 'Faces_logs',
            },
        ),
    ]
