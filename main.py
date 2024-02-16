import concurrent.futures
import creational_design_pattern.singleton.singleton as singleton
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(singleton.get_instance) for _ in range(5)]
        for future in concurrent.futures.as_completed(futures):
            future.result()
