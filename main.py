import concurrent.futures
import creational_design_pattern.singleton.singleton as singleton

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(2) as executor:
        futures = [executor.submit(singleton.get_instance, i) for i in range(10)]
        for future in concurrent.futures.as_completed(futures):
            future.result()
