USE [Fondinnehav_DB]
GO

/****** Object:  Table [dbo].[Stage_Fondinnehav]    Script Date: 2022-08-20 12:26:49 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Prod_Fondinnehav](
	[Tillgångsslag_enligt_LVF_5_kap] [varchar](max) NULL,
	[Instrumentnamn] [varchar](max) NULL,
	[ISIN_kod_instrument] [varchar](max) NULL,
	[Landkod_Emittent] [varchar](max) NULL,
	[Valuta] [varchar](max) NULL,
	[Bransch] [varchar](max) NULL,
	[Branschkod] [varchar](max) NULL,
	[Antal] [varchar](max) NULL,
	[Kurs] [varchar](max) NULL,
	[Valutakurs] [varchar](max) NULL,
	[Marknadsvärde] [varchar](max) NULL,
	[Andel av fond] [varchar](max) NULL,
	[unik_instrumend_id] [varchar](max) NULL,
	[Fond_institutnummer] [varchar](max) NULL,
	[Fond_ISIN] [varchar](max) NULL,
	[Fond_namn] [varchar](max) NULL,
	[Fond_status] [varchar](max) NULL,
	[unik_fond_id] [varchar](max) NULL,
	[Fondbolag_namn] [varchar](max) NULL,
	[Fondbolag_institutnummer] [varchar](max) NULL,
	[Fondbolag_LEI_kod] [varchar](max) NULL,
	[Kvartalsslut] [varchar](max) NULL,
	[Hash_key] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


