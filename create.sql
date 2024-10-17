IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 FIRST_ROW = 2,
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'dataset_finalproject111_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [dataset_finalproject111_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://dataset@finalproject111.dfs.core.windows.net' 
	)
GO

CREATE EXTERNAL TABLE AnnuallyDeaths (
	[Entity] nvarchar(4000),
	[Code] nvarchar(4000),
	[Year] bigint,
	[executions] bigint,
	[Meningitis] bigint,
	[Alzheimer] bigint,
	[Parkinson] bigint,
	[Nutritional_deficiencies] bigint,
	[Malaria] bigint,
	[Drowning] bigint,
	[Interpersonal violence] bigint,
	[Maternal disorders] bigint,
	[HIV] bigint,
	[Drug_use_disorders] bigint,
	[Tuberculosis] bigint,
	[Cardiovascular_diseases] bigint,
	[Lower_respiratory_infections] bigint,
	[Neonatal_disorders] bigint,
	[Alcohol_use_disorders] bigint,
	[Self_harm] bigint,
	[Exposure_to_forces_of_nature] bigint,
	[Diarrheal_diseases] bigint,
	[Environmental_heat_and_cold_exposure] bigint,
	[Neoplasms] bigint,
	[Conflict_and_terrorism] bigint,
	[Diabetes_mellitus] bigint,
	[Chronic_kidney_disease] bigint,
	[Poisonings] bigint,
	[Protein_energy_malnutrition] bigint,
	[Terrorism] bigint,
	[Road_injuries] bigint,
	[Chronic_respiratory_diseases] bigint,
	[Cirrhosis_and_other_chronic_liver_diseases] bigint,
	[Digestive_diseases] bigint,
	[Fire_heat_and_hot_substances] bigint,
	[Acute_hepatitis] bigint
	)
	WITH (
	LOCATION = 'annual-number-of-deaths-by-cause.csv',
	DATA_SOURCE = [dataset_finalproject111_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM AnnuallyDeaths
GO
