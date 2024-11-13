from django.db import models

class Company(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining primary key
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Dashboard(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining primary key
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Widget(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining primary key
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    widget_type = models.CharField(max_length=50, choices=[
        ('total_revenue', 'Общая выручка'),
        ('variable_expenses', 'Переменные расходы'),
        ('fixed_expenses', 'Постоянные расходы'),
        ('operating_profit', 'Операционная прибыль (EBITDA)'),
        ('net_profit', 'Чистая прибыль за период'),
        ('operational_profit_margin', 'Рентабельность по операционной прибыли, %'),
        ('debtor_liability', 'Дебиторская задолженность'),
        ('creditor_liability', 'Кредиторская задолженность'),
        ('turnover_days_debtors', 'Оборочиваемость д.з. (дни)'),
        ('turnover_days_creditors', 'Оборочиваемость к.з. (дни)'),
        ('cash_flow', 'Операционный денежный поток (OCF)'),
    ])
    position = models.IntegerField()
    data = models.TextField(blank=True, null=True)
