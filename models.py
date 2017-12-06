from django.db import models
from django.db.models import *
from django.template.defaultfilters import slugify
import datetime

class Agency(models.Model):
    agency_code = models.CharField(max_length=5, primary_key=True)
    agency_name = models.CharField(max_length=100)
    compensation_brd_com_members = models.DecimalField(max_digits=12, decimal_places=2)	
    cont_svc_incentive_plan_payments = models.DecimalField(max_digits=12, decimal_places=2)
    dp_signing_incentive_payments = models.DecimalField(max_digits=12, decimal_places=2)	
    education_loan_reimb_incentive = models.DecimalField(max_digits=12, decimal_places=2)
    employee_exp_allow_reportable = models.DecimalField(max_digits=12, decimal_places=2)
    holiday_pay_payroll_only = models.DecimalField(max_digits=12, decimal_places=2)
    indiv_incent_pay_safety_awds = models.DecimalField(max_digits=12, decimal_places=2)
    longevity_pay_h_ed = models.DecimalField(max_digits=12, decimal_places=2)
    longevity_pay_state_employees = models.DecimalField(max_digits=12, decimal_places=2)
    overtime_wages = models.DecimalField(max_digits=12, decimal_places=2)
    pay_differential = models.DecimalField(max_digits=12, decimal_places=2)
    sals_h_ed_non_prof_pay = models.DecimalField(max_digits=12, decimal_places=2)
    sals_h_ed_other_teach_pay = models.DecimalField(max_digits=12, decimal_places=2)
    sals_h_ed_prof_non_teach_pay = models.DecimalField(max_digits=12, decimal_places=2)
    sals_h_ed_teaching_pay = models.DecimalField(max_digits=12, decimal_places=2)
    sals_non_reg_pay = models.DecimalField(max_digits=12, decimal_places=2)
    sals_regular_pay = models.DecimalField(max_digits=12, decimal_places=2)
    sals_regular_pay_legislature = models.DecimalField(max_digits=12, decimal_places=2)
    signing_incent_pln_pmts_non_dp = models.DecimalField(max_digits=12, decimal_places=2)
    terminal_leave = models.DecimalField(max_digits=12, decimal_places=2)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2)
    name_slug = models.CharField(max_length=100)
   
        
    class Meta:
        db_table = u'salaries2017_agencies'

    def __unicode__(self):
        return self.agency_name

    def save(self):
	    self.name_slug = slugify(self.agency_name)
	    super(Agency, self).save()   

class Salary(models.Model):
    agency_code = models.ForeignKey(Agency)
    ocp_agency_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=150)
    hire_date = models.DateField(null=True, blank=True)
    gross_pay = models.DecimalField(max_digits=12, decimal_places=2)
    showhire = BooleanField()
    text = models.TextField()
    full_name = models.CharField(max_length=100)
    name_slug = models.CharField(max_length=200)

    class Meta:
        db_table = u'salaries2017'

    def save(self):
        self.full_name = '%s %s %s' % (self.first_name, self.middle_initial, self.last_name)
        self.name_slug = slugify(self.full_name)
        if self.hire_date > datetime.date(1900, 02, 01):
            self.showhire = True
        else:
            self.showhire = False
        super(Salary, self).save()
        
    def __unicode__(self):
        return self.full_name
