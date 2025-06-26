from config import ACLEDConfig
from pipeline import ACLEDPipeline

if __name__ == "__main__":
    config = ACLEDConfig.from_env()
    pipeline = ACLEDPipeline(config)
    pipeline.run()