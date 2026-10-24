import json
import os

class AmbiguityBenchmarkRunner:
    def __init__(self, dataset_path="bcnc_benchmark.json"):
        self.dataset_path = dataset_path
        self.dataset = self.load_dataset()

    def load_dataset(self):
        if not os.path.exists(self.dataset_path):
            print(f"Error: Dataset file '{self.dataset_path}' not found.")
            return []
        with open(self.dataset_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def print_dataset_summary(self):
        """Prints a statistical overview of the benchmark dataset."""
        print(f"=== BCNC Benchmark Summary ===")
        print(f"Total Test Cases Loaded: {len(self.dataset)}")
        
        domains = {}
        ambiguity_types = {}
        
        for item in self.dataset:
            dom = item.get("domain", "unknown")
            amb = item.get("ambiguity_type", "unknown")
            
            domains[dom] = domains.get(dom, 0) + 1
            ambiguity_types[amb] = ambiguity_types.get(amb, 0) + 1
            
        print("\nDomains breakdown:")
        for dom, count in domains.items():
            print(f" - {dom}: {count}")
            
        print("\nAmbiguity types breakdown:")
        for amb, count in ambiguity_types.items():
            print(f" - {amb}: {count}")
        print("==============================\n")

    def evaluate_model_mock(self, model_client=None):
        """
        Placeholder function to evaluate an LLM against the benchmark.
        In your actual research pipeline, you would pass your LLM response 
        here to check if it gracefully handles missing parameters or asks for clarification.
        """
        print("Running benchmark evaluation...")
        for item in self.dataset:
            print(f"[{item['id']}] Instruction: {item['bn_instruction']}")
            print(f" -> Expected Behavior: {item['expected_behavior']}")
            print(f" -> Missing Details Count: {len(item.get('missing_details', []))}")
            print("-" * 50)

if __name__ == "__main__":
    runner = AmbiguityBenchmarkRunner()
    if runner.dataset:
        runner.print_dataset_summary()
        runner.evaluate_model_mock()