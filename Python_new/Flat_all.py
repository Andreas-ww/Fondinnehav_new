

def read_quarters(quarter, engine):
    print("Hellos")
    #Import dependencies
    import csv
    import requests
    import xml.etree.ElementTree as ET
    import os
    import pandas as pd
    import sqlalchemy
    from sqlalchemy import create_engine
    from tqdm import trange, tqdm
    import re
    #Prefix
    prefix = '{http://schemas.fi.se/publika/vardepappersfonder/20200331}'

    
    fondbolag = os.listdir(quarter)
    fondbolag_path = [quarter + "/" + x for x in fondbolag]  # Path till alla fondbolag i kvartalet
    
    



    
    #Funktion för att gå igenom ett fondbolag 
    #fondbolaget_path = fondbolag_path[0]
    for fondbolaget_path in tqdm(fondbolag_path):
    
        
        fond = os.listdir(fondbolaget_path)
        fond_path = [fondbolaget_path+ "/" + x for x in fond] 
        
        #Funktion för att gå igenom en fond 
        #fonden_path = fond_path[2]
        #
        
        
        # instrument_df = pd.DataFrame()
        # full_instrument_df = pd.DataFrame()
        # instrument_rows = []
    
            
            
        for fonden_path in fond_path:
                    
            innehav_df = pd.DataFrame()
            full_innehav_df = pd.DataFrame()
            innehav_rows = []
            mega_df = pd.DataFrame()
    
            
           
            xmlparse = ET.parse(fonden_path)
            root = xmlparse.getroot()  
            
            
            
            
    
            
            fond_i = root.find(prefix+"Fondinformation")
            
          
            try:
                #Finansiella instrument nivås
                finans_intstrument_i = fond_i.find(prefix+"FinansiellaInstrument")
                #Lista med alla "children"/instrument i fonden
                fi_list = list(finans_intstrument_i)
                
                
                for instrument in fi_list:
    
                #Instrument dims       
                    Tillgangsslag_enligt_LVF_5_kap = instrument.find(prefix+"Tillgångsslag_enligt_LVF_5_kap").text if instrument.find(prefix+"Tillgångsslag_enligt_LVF_5_kap").text != None else "Saknad"
                    Instrumentnamn = instrument.find(prefix+"Instrumentnamn").text if instrument.find(prefix+"Instrumentnamn").text != None else "Saknad"
                    ISIN_kod_instrument = instrument.find(prefix+"ISIN-kod_instrument").text if instrument.find(prefix+"ISIN-kod_instrument").text != None else "Saknad"
                    Landkod_Emittent = instrument.find(prefix+"Landkod_Emittent").text if instrument.find(prefix+"Landkod_Emittent").text != None else "Saknad"
                    Valuta = instrument.find(prefix+"Valuta").text if instrument.find(prefix+"Valuta").text != None else "Saknad"
                    
                    try:
                        bransch = instrument.find(prefix+"Bransch")
                        branschkod_instrument = bransch.find(prefix+"Branschkod_instrument").text
                        bransch_namn = bransch.find(prefix+"Bransch_namn_instrument").text
                    except:
                        bransch = 'Saknad'
                        branschkod_instrument = 'Saknad'
                        bransch_namn = 'Saknad'
                        
                
                    
                    # instrument_rows.append({"Tillgångsslag_enligt_LVF_5_kap": Tillgangsslag_enligt_LVF_5_kap,
                    # 				"Instrumentnamn": Instrumentnamn,
                    # 				"ISIN_kod_instrument": ISIN_kod_instrument,
                    #           "Landkod_Emittent": Landkod_Emittent,
                    #           "Valuta": Valuta,
                    #             "Bransch": bransch_namn,
                    #             "Branschkod": branschkod_instrument,
                    #             "unik_instrumend_id": Instrumentnamn + ISIN_kod_instrument + Landkod_Emittent 
                    #             })
                    
                    #Innehav / Ownership                
                    antal = instrument.find(prefix+"Antal").text if instrument.find(prefix+"Antal").text != None else "Saknad"
                    kurs = instrument.find(prefix+"Kurs_som_använts_vid_värdering_av_instrumentet").text if instrument.find(prefix+"Kurs_som_använts_vid_värdering_av_instrumentet").text != None else "Saknad"
                    valutakurs = instrument.find(prefix+"Valutakurs_instrument").text  if instrument.find(prefix+"Valutakurs_instrument").text != None else "Saknad"
                    marknads_v = instrument.find(prefix+"Marknadsvärde_instrument").text  if instrument.find(prefix+"Marknadsvärde_instrument").text != None else "Saknad"
                    andel_av_fond = instrument.find(prefix+"Andel_av_fondförmögenhet_instrument").text  if instrument.find(prefix+"Andel_av_fondförmögenhet_instrument").text != None else "Saknad"
                    
                    innehav_rows.append({"Tillgångsslag_enligt_LVF_5_kap": Tillgangsslag_enligt_LVF_5_kap,
                    				    "Instrumentnamn": Instrumentnamn,
                        				"ISIN_kod_instrument": ISIN_kod_instrument,
                                        "Landkod_Emittent": Landkod_Emittent,
                                      "Valuta": Valuta,
                                        "Bransch": bransch_namn,
                                        "Branschkod": branschkod_instrument,
                                        "Antal":antal,
                                         "Kurs": kurs,
                                         "Valutakurs": valutakurs,
                                         "Marknadsvärde": marknads_v,
                                         "Andel av fond": andel_av_fond,
                                         "unik_instrumend_id": Instrumentnamn + ISIN_kod_instrument + Landkod_Emittent,
                                         })
                    
                    
                    
                    
                    
                innehav_df = pd.DataFrame(innehav_rows)
                
                #mega_df.append(innehav_df)
            
            
             
            except:
                print("inga instrument i " + fond_i.find(prefix+"Fond_namn").text)
            
            
            
            
            
            
            #
            #Till alla i fonden
            
            #Måste lägga till fler info 
            
            full_fond_df = pd.DataFrame()
            #LEI to join 
            fond_cols = ["Fond_institutnummer", "Fond_ISIN", "Fond_namn","Fondbolag_LEI_kod", "Fond_status"]
            fond_rows = []
            
            
            
            fond_i = root.find(prefix+"Fondinformation")
            Fond_institutnummer = fond_i.find(prefix+"Fond_institutnummer").text if fond_i.find(prefix+"Fond_institutnummer").text != None else "Saknad"
            Fond_ISIN = fond_i.find(prefix+"Fond_ISIN-kod").text if fond_i.find(prefix+"Fond_ISIN-kod").text != None else "Saknad"
            Fond_namn = fond_i.find(prefix+"Fond_namn").text  if fond_i.find(prefix+"Fond_namn").text  != None else "Saknad"
            
            try:
                Fond_status = fond_i.find(prefix+"Fond_status").text
            
                fond_rows.append({"Fond_institutnummer": Fond_institutnummer,
                				"Fond_ISIN": Fond_ISIN,
                				"Fond_namn": Fond_namn,
                         "Fond_status": Fond_status,
                         "unik_fond_id": Fond_namn + Fond_ISIN + Fond_institutnummer
                         }
                         )
            except:
                fond_rows.append({"Fond_institutnummer": Fond_institutnummer,
                				"Fond_ISIN": Fond_ISIN,
                				"Fond_namn": Fond_namn,
                         "Fond_status": "Aktiv",
                         "unik_fond_id": Fond_namn + Fond_ISIN + Fond_institutnummer}
                         )
                
            fond_df = pd.DataFrame(fond_rows)
            fond_df.Fond_institutnummer = fond_df.Fond_institutnummer.str.strip()
            
            
            full_fond_df = full_fond_df.append(fond_df) 
            
            #
            
            #
            #Till alla i bolaget 
            full_bolag_df = pd.DataFrame()
            bolag_cols = ["Fondbolag_namn", "Fondbolag_institutnummer", "Fondbolag_LEI_kod"]
            bolag_rows = []
            
            #Get info
            bolags_i = root.find(prefix+"Bolagsinformation")
            Fondbolag_namn = bolags_i.find(prefix+"Fondbolag_namn").text  if bolags_i.find(prefix+"Fondbolag_namn").text != None else "Saknad"
            Fondbolag_institutnummer = bolags_i.find(prefix+"Fondbolag_institutnummer").text  if bolags_i.find(prefix+"Fondbolag_institutnummer").text  != None else "Saknad"
            LEI = bolags_i.find(prefix+"Fondbolag_LEI-kod").text  if bolags_i.find(prefix+"Fondbolag_LEI-kod").text != None else "Saknad"
            
                   
            bolag_rows.append({"Fondbolag_namn": Fondbolag_namn,
                    				"Fondbolag_institutnummer": Fondbolag_institutnummer,
                    				"Fondbolag_LEI_kod": LEI})
                    
            bolag_df = pd.DataFrame(bolag_rows, columns=bolag_cols)
            
            
            #
            #Till alla i kvartalet 
            #Rapportinfo: kvartalsslut
            rapport_i = root.find(prefix+"Rapportinformation")    
            #Date for registration
            kvartalsslut=rapport_i.find(prefix + "Kvartalsslut").text  if rapport_i.find(prefix + "Kvartalsslut").text != None else "Saknad"
            
            kvartallslut_df = pd.DataFrame()
            
            #
            mega_df = mega_df.append(innehav_df)
            
            mega_df = mega_df.merge(fond_df,how='cross')
            
            mega_df = mega_df.merge(bolag_df, how='cross')
            
            kv = {'Kvartalsslut':[kvartalsslut]}
            mega_df = mega_df.merge(pd.DataFrame(kv), how='cross')
            
            mega_df.to_csv("C:/Users/awestroth/Privat/Fondinnehav_github/Test_ou_tables/"  + Fondbolag_namn + re.sub(r'[^a-zA-Z]', '', Fond_namn) + ".csv", encoding='utf-8')

            mega_df.to_sql("Stage_Fondinnehav",engine, if_exists="append", index=False)

        
    return         print("Quarter: " + kvartalsslut + "Is done")
