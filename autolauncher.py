#prerequesite#
import virtualbox

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
#The vm name in my case is : "pi"
machine = vbox.find_machine("Pi")
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion() 