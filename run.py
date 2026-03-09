import sys
import os
import subprocess
from pathlib import Path

def main():
    lld_dir = Path('lld')
    
    if len(sys.argv) < 2:
        print("Usage: python run.py <concept_name>")
        print("Example: python run.py strategy_pattern")
        
        print("\nAvailable practice files in 'lld/':")
        found = False
        if lld_dir.exists():
            for filepath in lld_dir.rglob('*_practice.py'):
                # Extract the concept name by removing '_practice.py'
                concept_name = filepath.name.replace('_practice.py', '')
                print(f"  - {concept_name} (found in {filepath.parent})")
                found = True
        
        if not found:
            print("  (No practice files found in 'lld/' directory)")
        sys.exit(1)

    concept_name = sys.argv[1]
    
    # Strip suffixes if the user accidentally included them
    if concept_name.endswith('.py'):
        concept_name = concept_name[:-3]
    if concept_name.endswith('_practice'):
        concept_name = concept_name[:-9]

    expected_filename = f"{concept_name}_practice.py"
    
    # Search for the file in the lld directory
    target_file = None
    if lld_dir.exists():
        for filepath in lld_dir.rglob(expected_filename):
            target_file = filepath
            break

    if not target_file:
        print(f"Error: Could not find file '{expected_filename}' anywhere inside the 'lld/' directory.")
        sys.exit(1)

    print(f"========== Running {target_file} ==========\n")
    try:
        # Run the target python file as a separate process
        subprocess.run([sys.executable, str(target_file)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Execution failed with return code {e.returncode}")
    except KeyboardInterrupt:
        print("\n[!] Execution interrupted by user")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
    finally:
        print("\n=======================================================")

if __name__ == "__main__":
    main()
