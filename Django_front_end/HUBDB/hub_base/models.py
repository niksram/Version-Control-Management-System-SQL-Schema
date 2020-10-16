from django.db import models


class Coder(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    type = models.CharField(max_length=10)
    company = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coder'


class Commits(models.Model):
    time_stamp = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    repo_name = models.ForeignKey('Repository', models.DO_NOTHING, db_column='repo_name', blank=True, null=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    file_extension = models.ForeignKey('Extension', models.DO_NOTHING, db_column='file_extension', blank=True, null=True)
    contributor = models.ForeignKey(Coder, models.DO_NOTHING, db_column='contributor', blank=True, null=True)
    commit_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'commits'


class Employee(models.Model):
    e_id = models.CharField(primary_key=True, max_length=13)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    job_desc = models.ForeignKey('Salary', models.DO_NOTHING, db_column='job_desc', blank=True, null=True)
    ip = models.ForeignKey('Server', models.DO_NOTHING, db_column='ip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Extension(models.Model):
    extension = models.CharField(primary_key=True, max_length=10)
    file_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extension'


class Files(models.Model):
    file_name = models.CharField(primary_key=True, max_length=50)
    file_extension = models.ForeignKey(Extension, models.DO_NOTHING, db_column='file_extension')
    repo_name = models.ForeignKey('Repository', models.DO_NOTHING, db_column='repo_name')
    contributor = models.ForeignKey(Coder, models.DO_NOTHING, db_column='contributor', blank=True, null=True)
    size = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'files'
        unique_together = (('file_name', 'repo_name', 'file_extension'),)


class Repository(models.Model):
    repo_name = models.CharField(primary_key=True, max_length=50)
    owner_username = models.ForeignKey(Coder, models.DO_NOTHING, db_column='owner_username')
    description = models.CharField(max_length=100, blank=True, null=True)
    ip = models.ForeignKey('Server', models.DO_NOTHING, db_column='ip')
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repository'


class Salary(models.Model):
    job_desc = models.CharField(primary_key=True, max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'salary'


class Server(models.Model):
    ip = models.CharField(primary_key=True, max_length=15)
    location = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'server'


class Starred(models.Model):
    username = models.OneToOneField(Coder, models.DO_NOTHING, db_column='username', primary_key=True)
    repo_name = models.ForeignKey(Repository, models.DO_NOTHING, db_column='repo_name')
    rating = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'starred'
        unique_together = (('username', 'repo_name'),)