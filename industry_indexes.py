# Mapping industries to sub-indexes
industry_sub_indexes = {
    'Capital Markets': ['^SP500-40'],  # S&P 500 Financials Index, tracks capital market firms like investment banks and brokerages
    'Consumer Electronics': ['^SP500-45', '^DJI', '^IXIC'],  # S&P 500 Information Technology Index, Dow Jones Industrial Average, Nasdaq Composite Index
    'Oil & Gas Integrated': ['^XOI', '^OEX'],  # PHLX Oil Service Index, S&P 100 Index, tracks integrated oil and gas companies
    'REIT - Specialty': ['^RMZ', '^SP500-60'],  # MSCI U.S. REIT Index, S&P 500 Real Estate Index, tracks specialty real estate investment trusts
    'Integrated Freight & Logistics': ['^DJT', '^TRAN', '^SP500-20'],  # Dow Jones Transportation Average, AMEX Transportation Average, S&P 500 Industrials Index
    'Insurance - Diversified': ['^SP500-40', '^SP500-60'],  # S&P 500 Financials, S&P Insurance Select Industry Index, tracks diversified insurance firms
    'Drug Manufacturers - General': ['^SP500-35'],  # S&P 500 Healthcare Index, includes general drug manufacturers
    'Aerospace & Defense': ['^SP500-20'],  # S&P 500 Industrials Index, includes aerospace and defense companies
    'Semiconductors': ['^SOX', '^SP500-35', '^SP500-45'],  # PHLX Semiconductor Index, S&P 500 Healthcare, S&P 500 Information Technology Index
    'Specialty Chemicals': ['^DJUSCH', '^SP500-15'],  # Dow Jones U.S. Chemicals Index, S&P 500 Materials Index, tracks specialty chemical companies
    'Farm & Heavy Construction Machinery': ['^SP500-20'],  # S&P 500 Industrials Index, includes construction and heavy machinery firms
    'Entertainment': ['^SP500-55', '^SP500-50'],  # S&P 500 Media & Entertainment Index, S&P 500 Communication Services Sector Index
    'Internet Retail': ['^SP500-25', 'IXIC'],  # S&P 500 Consumer Discretionary Index, tracks internet retail companies
    'Household & Personal Products': ['^SP500-30'],  # S&P 500 Consumer Staples Index, tracks household and personal product companies
    'Internet Content & Information': ['^NDXT', '^SP500-50'],  # Nasdaq Internet Index, S&P 500 Communication Services Sector Index, tracks internet content firms
    'Software - Infrastructure': ['^SP500-45'],  # S&P 500 Information Technology Sector Index, includes software infrastructure firms
    'Auto Manufacturers': ['^SP500-25', 'CARZ'],  # S&P 500 Consumer Discretionary Index, iShares U.S. Automobiles & Parts ETF, tracks automobile manufacturers
    'Beverages - Non-Alcoholic': ['^SP500-30'],  # S&P 500 Consumer Staples Index, includes non-alcoholic beverage companies
}

'''
Ticker Examples for Each Industry:

Capital Markets: GS (The Goldman Sachs Group, Inc.) 
Consumer Electronics: AAPL
Oil & Gas Integrated: XOM (Exxon Mobil Corporation) 
REIT - Specialty: SPG (Simon Property Group, Inc.), AMT (American Tower Corporation)
Integrated Freight & Logistics: UPS (United Parcel Service, Inc.) 
Insurance - Diversified: BRK-B
Drug Manufacturers - General: AMGN (Amgen Inc.), PFE (Pfizer Inc.)
Aerospace & Defense: LMT (Lockheed Martin Corporation)
Semiconductors: NVDA, AMD
Specialty Chemicals: DD (DuPont de Nemours, Inc.)
Farm & Heavy Construction Machinery: CAT (Caterpillar Inc.)
Entertainment: NFLX
Internet Retail: AMZN
Household & Personal Products: PG (The Procter & Gamble Company)
Internet Content & Information: GOOG, META
Software - Infrastructure: MSFT, PLTR
Auto Manufacturers: F (Ford Motor Company), TSLA
Beverages - Non-Alcoholic: PEP (PepsiCo, Inc.), KO (The Coca-Cola Company)
'''