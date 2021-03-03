#prerequesite#
import virtualbox

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
#The vm name in my case is : "pi"
machine = vbox.find_machine("Pi")
# progress = machine.launch_vm_process(session, "gui", "")
# For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion() 