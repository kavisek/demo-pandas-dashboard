import json
import numpy as np
import pandas as pd
import redis
import time


class ProducerPipeline:
    def start_connection(self) -> None:
        """Initialize a redis database connection."""
        # The redis host, port, and password are specified in the docker compose folder.
        self.r = redis.Redis(
            host="pandas-dashboard_redis_1", port="6379", password="demo"
        )

    def run(self) -> None:
        """A function that that run the pipeline and send some random
        data to redis.
        """

        # Generate test data.
        options = [f"player_{i}" for i in range(10)]
        df = pd.DataFrame(
            {
                "player": np.random.choice(options, 5),
                "score": np.random.randint(100, size=5),
                "season_average": np.random.randint(100, size=5),
            }
        )

        # Convert dataaframe to dicitonary.
        data = df.to_dict()

        # Convert dictionary to string representation of string.
        json_data = json.dumps(data)
        self.r.set("dashboard_data", json_data)

        # Log results.
        print("finsihed loading data into cache.")
        print(f"value: {json_data}")


def main():
    # Start producer pipeline.
    Producer = ProducerPipeline()
    Producer.start_connection()

    # Run the pipeline in a loop.
    while True:
        Producer.run()
        time.sleep(30)


if __name__ == "__main__":
    main()
