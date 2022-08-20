INSERT INTO [Fondinnehav_DB].[dbo].[Prod_Fondinnehav]
SELECT * FROM [Fondinnehav_DB].[dbo].[vw_Stage_Fondinnehav] as vw
WHERE vw.Hash_key NOT IN ( SELECT Hash_key FROM [Fondinnehav_DB].[dbo].[Prod_Fondinnehav])