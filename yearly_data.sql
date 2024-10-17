Select Year , sum(Interpersonal_violence), 
sum(Maternal_disorders) 
sum(Drug_use_disorders),  
sum(Alcohol_use_disorders), 
sum(Self_harm) 
FROM annual_deaths_only
Group by Year 
GO

# mental disorder increase over years

Select Year , SUM(Drowning) ,
SUM(Road_injuries)
SUM(Fire_heat_and_hot_substances)
SUM(Exposure_to_forces_of_nature)
SUM(Environmental_heat_and_cold_exposure) 
FROM annual_deaths_only
Group by Year 
GO

# Accidents and External Causes Decrease compared to population increase


Select Year ,
SUM(Alzheimer)
SUM(Parkinson),
SUM(Cardiovascular_diseases),
SUM(Neoplasms),
SUM(Diabetes_mellitus),
SUM(Chronic_kidney_disease),
SUM(Chronic_respiratory_diseases),
SUM(Cirrhosis_and_other_chronic_liver_diseases),
SUM(Digestive_diseases)
FROM annual_deaths_only
Group by Year 
GO


# Chronic Diseases decreased

