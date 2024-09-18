#!/usr/bin/env python3
""" Module for DataPipeline class"""

import pandas as pd
from pymongo import MongoClient
import boto3


class DataPipeline:
    """DataPipeline class"""
    def __init__(self):
        self.mongo_client = MongoClient('mongodb://localhost:27017/')
        self.s3_client = boto3.client('s3')

    def extract_data(self):
        db = self.mongo_client['teched_pipeline']
        student_data = pd.DataFrame(list(db.student_performance.find()))
        return student_data

    def transform_data(self, data):
        # Implement data transformation logic
        transformed_data = data  # Placeholder for actual transformation
        return transformed_data

    def load_data(self, data, bucket_name, file_name):
        csv_buffer = data.to_csv(index=False)
        self.s3_client.put_object(
                                  Bucket=bucket_name,
                                  Key=file_name,
                                  Body=csv_buffer)

    def run_pipeline(self):
        raw_data = self.extract_data()
        transformed_data = self.transform_data(raw_data)
        self.load_data(
                       transformed_data,
                       'teched-pipeline-bucket',
                       'student_performance.csv')

"""
# Usage
pipeline = DataPipeline()
pipeline.run_pipeline()
"""
