USE [Fondinnehav_DB]
GO

/****** Object:  View [dbo].[vw_Stage_Fondinnehav]    Script Date: 2022-08-20 12:45:12 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

/****** Script for SelectTopNRows command from SSMS  ******/
CREATE OR ALTER   view [dbo].[vw_Stage_Fondinnehav] as(
SELECT  [Tillgångsslag_enligt_LVF_5_kap]
      ,[Instrumentnamn]
      ,[ISIN_kod_instrument]
      ,[Landkod_Emittent]
      ,[Valuta]
      ,[Bransch]
      ,[Branschkod]
      ,[Antal]
      ,[Kurs]
      ,[Valutakurs]
      ,[Marknadsvärde]
      ,[Andel av fond]
      ,[unik_instrumend_id]
      ,[Fond_institutnummer]
      ,[Fond_ISIN]
      ,[Fond_namn]
      ,[Fond_status]
      ,[unik_fond_id]
      ,[Fondbolag_namn]
      ,[Fondbolag_institutnummer]
      ,[Fondbolag_LEI_kod]
      ,[Kvartalsslut]
	  ,HASHBYTES('SHA2_512',
		[Tillgångsslag_enligt_LVF_5_kap]
      +[Instrumentnamn]
      +[ISIN_kod_instrument]
      +[Landkod_Emittent]
      +[Valuta]
      +[Bransch]
      +[Branschkod]
      +[Antal]
      +[Kurs]
      +[Valutakurs]
      +[Marknadsvärde]
      +[Andel av fond]
      +[unik_instrumend_id]
      +[Fond_institutnummer]
      +[Fond_ISIN]
      +[Fond_namn]
      +[Fond_status]
      +[unik_fond_id]
      +[Fondbolag_namn]
      +[Fondbolag_institutnummer]
      +[Fondbolag_LEI_kod]
      +[Kvartalsslut]) Hash_key
  FROM [Fondinnehav_DB].[dbo].[Stage_Fondinnehav]
  )
GO


