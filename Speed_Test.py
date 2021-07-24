import speedtest

test = speedtest.Speedtest()

print("Loading server Lit...")
test.get_servers() # To get list of servers
print("Chossing best server...")
best = test.get_best_server() #To choose best server

print(best)
print(f"Found: {best['host']} located:{best['country']}")

print("Performing download test...")
download_result = test.download()
print("Performing upload test...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download speed: {download_result/ 1024 / 1024 :.2f}Mbit/s")
print(f"upload speed: {upload_result/ 1024 / 1024 :.2f}Mbit/s")
print(f"ping: {download_result:.2f} ms")