import os
import json
from kernel.settings.core.logs import configure_logging
from painless.utils.funcs import create_directories
from kernel.settings import config
import logging
import pandas as pd
from my_elasticsearch import ElasticConnector

coreLogger = logging.getLogger('core')


ELASTIC_HOST = config.get_value('elasticsearch', 'HOST')

es_connector = ElasticConnector(host=ELASTIC_HOST)


def main():
    base_dir_path = os.path.dirname(os.path.abspath(__file__))
    LOG_DIRECTORIES = config.get_value('log', 'LOG_DIRS')
    CONFIGS_LOG_DIRECTORIES = config.get_value('log', 'CONFIG_PATH')
    create_directories(base_dir=base_dir_path, directories=LOG_DIRECTORIES)
    configure_logging(CONFIGS_LOG_DIRECTORIES)

    # coreLogger.warning("Invalid instance received in set_token_status signal")

    # with open('C:/Users/Admin/Desktop/PROJECT/python_elasticsearch/python/importer/data/file_sources/mapping.json', 'r') as file:
    #     mapping = json.load(file)

    # a = es_connector.create_index('country', body=mapping)

    # df = pd.read_csv(
    #     'C:/Users/Admin/Desktop/PROJECT/python_elasticsearch/python/importer/data/file_sources/country.csv')

    # for index, row in df.iterrows():
    #     document = row.to_dict()
    #     es_connector.insert_document(index_name='country', document=document)



    # region : "Africa" 
    query = {
        "query": {
            "match": {
                "region": "Africa"

            }
        }
    }

    # region : "Europe"  or name : "Antigua and Barbuda" 
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"region": "Europe"}},
                    {"match": {"name": "Antigua and Barbuda"}}
                ]
            }
        }

    }

    # region : "Europe" and name : "Jersey" 
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"region": "Europe"}},
                    {"match": {"name": "Jersey"}}
                ]
            }
        }
    }

    # region : "Cuba" or : "Cuba"
    query = {
        "query": {
            "multi_match": {
                "query": "Cuba",
                "fields": ["name", "region"]
            }
        }
    }


    # query = {
    #     "size": 0,
    #     "aggs": {
    #         "region_count": {
    #             "terms": {
    #                 "field": "region"
    #             }
    #         }
    #     }
    # }

    # query = {
    #     "size": 0,
    #     "aggs": {
    #         "region_count": {
    #             "terms": {
    #                 "field": "region"
    #             },
    #             "aggs": {
    #                 "ava_region_code": {
    #                     "avg": {
    #                         "field": "sub-region-code"
    #                     }
    #                 },
    #                 "max_region_code": {
    #                     "max": {
    #                         "field": "sub-region-code"
    #                     }
    #                 },
    #                 "min_region_code": {
    #                     "min": {
    #                         "field": "sub-region-code"
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }



    response = es_connector.search(index='country', body=query)

    for hit in response['hits']['hits']:
        print(hit['_source'])

    # for hit in response['aggregations']['region_count']['buckets']:
    #     print(hit)


if __name__ == "__main__":
    main()
