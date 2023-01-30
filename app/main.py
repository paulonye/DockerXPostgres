#!/usr/bin/env python3
import pandas as pd
from connect import get_connection
from scrape import capture_data

def main():

    df = capture_data()

    engine = get_connection()

    df.to_sql(name = 'yahoofinance', con = engine, if_exists = 'append')
    
    engine.connect().close()


if __name__ == '__main__':
    main()