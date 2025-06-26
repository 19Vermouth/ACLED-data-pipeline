from config import ACLEDConfig
from extractors import ACLEDExtractor
from transformers import ACLEDTransformer
from loaders import ACLEDLoader
from visualizers import ACLEDVisualizer

class ACLEDPipeline:
    def __init__(self, config: ACLEDConfig):
        self.config = config
        self.extractor = ACLEDExtractor(config)
        self.transformer = ACLEDTransformer()
        self.loader = ACLEDLoader()
        self.visualizer = ACLEDVisualizer()

    def run(self):
        print("🚀 Starting ACLED Data Pipeline...")
        print("=" * 50)

        test_response = self.extractor.test_api_connection()
        if test_response.success:
            print("\n" + "=" * 50)
            response = self.extractor.extract_data()
            if response.success and not response.data.empty:
                transformed_df = self.transformer.transform_data(response.data)
                self.loader.load_to_db(transformed_df)
                self.visualizer.visualize_data(transformed_df)
                self.visualizer.map_conflicts(transformed_df)
                print("\n🎉 Pipeline completed successfully!")
            else:
                print("\n❌ Pipeline failed: No data extracted")
        else:
            print("\n❌ Cannot proceed - API authentication failed")
            print("Please check your email and API key in .env")