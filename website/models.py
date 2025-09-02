from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    simulation_name = models.CharField(max_length=50)
    weatherfile_name = models.CharField(max_length=50)
    run_period = models.CharField(max_length=100)
    total_cooling_energy = models.CharField(max_length=15)
    peak_cooling_load = models.CharField(max_length=15)
    reporting_interval = models.CharField(max_length=20)
    cooling_setpoint = models.CharField(max_length=20)
    cooling_schedule_type = models.CharField(max_length=50)
    system_cop = models.CharField(max_length=20)
    operation_schedule_type = models.CharField(max_length=60)
    lighting_energy = models.CharField(max_length=20)
    equipment_energy = models.CharField(max_length=20)
    envelope_properties = models.CharField(max_length=20)
    eui = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.simulation_name} {self.weatherfile_name}")
