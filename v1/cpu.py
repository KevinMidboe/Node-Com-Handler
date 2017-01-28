import linuxcpureader

def main():
	cpu = linuxcpureader.LinuxCpuTemperatureReader()
	print(cpu)
	print(cpu.get_reader())
	print(', '.join("%s: %s" % item for item in cpu.items()))

main() 
