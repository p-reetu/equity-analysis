# Generated by Django 3.1.7 on 2021-05-16 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_sheet_stockedge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Financials', models.CharField(default='-', max_length=100)),
                ('Particulars', models.CharField(default='-', max_length=200)),
                ('Shh_Funds', models.CharField(default='-', max_length=100)),
                ('Non_Curr_Liab', models.CharField(default='-', max_length=100)),
                ('Curr_Liab', models.CharField(default='-', max_length=100)),
                ('Minority_Int', models.CharField(default='-', max_length=100)),
                ('Equity_and_Liab', models.CharField(default='-', max_length=100)),
                ('Non_Curr_Assets', models.CharField(default='-', max_length=100)),
                ('Curr_Assets', models.CharField(default='-', max_length=100)),
                ('Misc_Exp_not_WO', models.CharField(default='-', max_length=100)),
                ('Total_Assets', models.CharField(default='-', max_length=100)),
                ('Website', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='balance_sheet_ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Financial_Year', models.CharField(default='-', max_length=100)),
                ('Cash_and_Short_Term_Investments', models.CharField(default='-', max_length=100)),
                ('Total_Receivables', models.CharField(default='-', max_length=100)),
                ('Total_Inventory', models.CharField(default='-', max_length=100)),
                ('Other_Current_Assets', models.CharField(default='-', max_length=100)),
                ('Current_Assets', models.CharField(default='-', max_length=100)),
                ('Loans_and_Advances', models.CharField(default='-', max_length=100)),
                ('Net_PropertyPlantEquipment', models.CharField(default='-', max_length=100)),
                ('Goodwill_and_Intangibles', models.CharField(default='-', max_length=100)),
                ('Long_Term_Investments', models.CharField(default='-', max_length=100)),
                ('Deferred_Tax_Assets_Net', models.CharField(default='-', max_length=100)),
                ('Other_Assets', models.CharField(default='-', max_length=100)),
                ('Non_Current_Assets', models.CharField(default='-', max_length=100)),
                ('Total_Assets', models.CharField(default='-', max_length=100)),
                ('Accounts_Payable', models.CharField(default='-', max_length=100)),
                ('Total_Deposits', models.CharField(default='-', max_length=100)),
                ('Other_Current_Liabilities', models.CharField(default='-', max_length=100)),
                ('Current_Liabilities', models.CharField(default='-', max_length=100)),
                ('Total_Long_Term_Debt', models.CharField(default='-', max_length=100)),
                ('Deferred_Tax_Liabilities_Net', models.CharField(default='-', max_length=100)),
                ('Other_Liabilities', models.CharField(default='-', max_length=100)),
                ('Non_Current_Liabilities', models.CharField(default='-', max_length=100)),
                ('Total_Liabilities', models.CharField(default='-', max_length=100)),
                ('Common_Stock', models.CharField(default='-', max_length=100)),
                ('Additional_Paid_in_Capital', models.CharField(default='-', max_length=100)),
                ('Reserves_and_Surplus', models.CharField(default='-', max_length=100)),
                ('Minority_Interest', models.CharField(default='-', max_length=100)),
                ('Other_Equity', models.CharField(default='-', max_length=100)),
                ('Total_Equity', models.CharField(default='-', max_length=100)),
                ('Total_Liabilities_and_Shareholders_Equity', models.CharField(default='-', max_length=100)),
                ('Total_Common_Shares_Outstanding', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cash_Flow_stockedge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Financials', models.CharField(default='-', max_length=100)),
                ('Particulars', models.CharField(default='-', max_length=1100)),
                ('Cash_Fr_Operatn', models.CharField(default='-', max_length=100)),
                ('Cash_Fr_Inv', models.CharField(default='-', max_length=100)),
                ('Cash_Fr_Finan', models.CharField(default='-', max_length=100)),
                ('Net_Change', models.CharField(default='-', max_length=100)),
                ('Cash_and_Cash_Eqvt', models.CharField(default='-', max_length=100)),
                ('Website', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cashflow_ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Financial_Year', models.CharField(default='-', max_length=100)),
                ('Cash_from_Operating_Activities', models.CharField(default='-', max_length=100)),
                ('Cash_from_Investing_Activities', models.CharField(default='-', max_length=100)),
                ('Cash_from_Financing_Activities', models.CharField(default='-', max_length=100)),
                ('Net_Change_in_Cash', models.CharField(default='-', max_length=100)),
                ('Changes_in_Working_Capital', models.CharField(default='-', max_length=100)),
                ('Capital_Expenditures', models.CharField(default='-', max_length=100)),
                ('Free_Cash_Flow', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('symbol', models.CharField(default='unavailable', max_length=20, primary_key=True, serialize=False)),
                ('company_name', models.CharField(default='-', max_length=100)),
                ('logo', models.TextField(default='No logo')),
                ('description', models.TextField(default='no info')),
                ('description_wiki', models.TextField(default='no info')),
                ('financial_report', models.TextField(default='no info')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Indicators_stockedge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Fundamental', models.CharField(default='-', max_length=100)),
                ('Price', models.CharField(default='-', max_length=100)),
                ('Market_Cap', models.CharField(default='-', max_length=100)),
                ('Earnings_per_share_EPS', models.CharField(default='-', max_length=100)),
                ('Price_Earning_Ratio_PE', models.CharField(default='-', max_length=100)),
                ('Industry_PE', models.CharField(default='-', max_length=100)),
                ('Book_Value_Share', models.CharField(default='-', max_length=100)),
                ('Price_to_Book_Value', models.CharField(default='-', max_length=100)),
                ('Dividend_Yield', models.CharField(default='-', max_length=100)),
                ('No_of_Shares_Subscribed', models.CharField(default='-', max_length=100)),
                ('FaceValue', models.CharField(default='-', max_length=100)),
                ('Website', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='income_ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Financial_Year', models.CharField(default='-', max_length=100)),
                ('Total_Revenue', models.CharField(default='-', max_length=100)),
                ('Raw_Materials', models.CharField(default='-', max_length=100)),
                ('Power_and_Fuel_Cost', models.CharField(default='-', max_length=100)),
                ('Employee_Cost', models.CharField(default='-', max_length=100)),
                ('Selling_and_Administrative_Expenses', models.CharField(default='-', max_length=100)),
                ('Operating_and_Other_expenses', models.CharField(default='-', max_length=100)),
                ('EBITDA', models.CharField(default='-', max_length=100)),
                ('DepreciationAmortization', models.CharField(default='-', max_length=100)),
                ('PBIT', models.CharField(default='-', max_length=100)),
                ('Interest_and_Other_Items', models.CharField(default='-', max_length=100)),
                ('PBT', models.CharField(default='-', max_length=100)),
                ('Taxes_and_Other_Items', models.CharField(default='-', max_length=100)),
                ('Net_Income', models.CharField(default='-', max_length=100)),
                ('EPS', models.CharField(default='-', max_length=100)),
                ('DPS', models.CharField(default='-', max_length=100)),
                ('Payout_ratio', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Overview_stockedge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Fundamental', models.CharField(default='-', max_length=100)),
                ('Sector', models.CharField(default='-', max_length=100)),
                ('Industry', models.CharField(default='-', max_length=100)),
                ('Website', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pattern_stockedge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Shareholding', models.CharField(default='-', max_length=100)),
                ('Qtrs', models.CharField(max_length=200)),
                ('Promoter', models.CharField(default='-', max_length=100)),
                ('Public', models.CharField(default='-', max_length=100)),
                ('FIIFPI', models.CharField(default='-', max_length=100)),
                ('DII', models.CharField(default='-', max_length=100)),
                ('Non_Institution', models.CharField(default='-', max_length=100)),
                ('Depository_Receipts', models.CharField(default='-', max_length=100)),
                ('Promoter_Holding_Pledge', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='peers_ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Stock', models.CharField(default='-', max_length=100)),
                ('Asian_Paints_Ltd', models.CharField(default='-', max_length=100)),
                ('Berger_Paints_India_Ltd', models.CharField(default='-', max_length=100)),
                ('Kansai_Nerolac_Paints_Ltd', models.CharField(default='-', max_length=100)),
                ('Indigo_Paints_Ltd', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profit_and_Loss_stockedge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='unavailable', max_length=15)),
                ('Financials', models.CharField(default='-', max_length=100)),
                ('Particulars', models.CharField(default='-', max_length=100)),
                ('Net_Sales', models.CharField(default='-', max_length=100)),
                ('Other_Income', models.CharField(default='-', max_length=100)),
                ('Total_Income', models.CharField(default='-', max_length=100)),
                ('Total_Expenditure', models.CharField(default='-', max_length=100)),
                ('PBIDT', models.CharField(default='-', max_length=100)),
                ('Interest', models.CharField(default='-', max_length=100)),
                ('Depreciation', models.CharField(default='-', max_length=100)),
                ('Taxation', models.CharField(default='-', max_length=100)),
                ('Exceptional_Items', models.CharField(default='-', max_length=100)),
                ('PAT', models.CharField(default='-', max_length=100)),
                ('Website', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(default='-', max_length=100)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('Username', models.CharField(default='-', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='-', max_length=60)),
            ],
        ),
    ]
