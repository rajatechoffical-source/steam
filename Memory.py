from flask import *
import threading
import keyboard
from datetime import datetime

import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
# from aob import *


from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os


def mkp(aob: str):
    if '??' in aob:
        if aob.startswith("??"):
            aob = f" {aob}"
            n = aob.replace(" ??", ".").replace(" ", "\\x")
            b = bytes(n.encode())
        else:
            n = aob.replace(" ??", ".").replace(" ", "\\x")
            b = bytes(f"\\x{n}".encode())
        del n
        return b
    else:
        m = aob.replace(" ", "\\x")
        c = bytes(f"\\x{m}".encode())
        del m
        return c
    


def HEADLOAD():
    try:

        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        return

    try:
        if proc:
            print("\033[31m[>]\033[0m Searching Entity...")
            
            global aimbot_addresses
            entity_pattern = mkp("FF FF ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? FF FF FF FF FF FF FF FF ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? A5 43 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 80 BF ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 80 3F ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 80 3F")
            aimbot_addresses = pattern_scan_all(proc.process_handle, entity_pattern, return_multiple=True)

            if aimbot_addresses:
                print("Addresses found")
                
            else:
                print("Failed")
    
    except:
        print("")
    finally:
        if proc:
            proc.close_process()
    return "Fitur Berhasil Di Load"
    


def HEADON():
    try:
        proc = Pymem("HD-Player")
    
        if proc:
            global original_value
            original_value = []
            for current_entity in aimbot_addresses:
                original_value.append((current_entity, read_bytes(proc.process_handle, current_entity + 0x9E, 4)))
                # Read the value at current_entity + 0x60
                # Read the value at current_entity + 0x2C
                value_bytes = read_bytes(proc.process_handle, current_entity +  0xA2, 4) 
                
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, current_entity + 0x9E, value_bytes, len(value_bytes))
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
           
    return "AIMBOT HEAD ON"

def HEADOFF():
    try:
        # Open the process
        proc = Pymem("HD-Player")
        
        if original_value:
         
            for i in original_value:
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, i[0] + 0x9E, i[1], len(i[1]))
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
    return "AIMBOT HEAD OFF"


def RIGHTSHOULDERON():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    
        if proc:
            global original_value
            # Save the original value to variable, btw all the orginal values are same so we just save one
            original_value = []
            for current_entity in aimbot_addresses:
                original_value.append((current_entity, read_bytes(proc.process_handle, current_entity + 0x9E, 4)))
                # Read the value at current_entity + 0x60
                # Read the value at current_entity + 0x2C
                value_bytes = read_bytes(proc.process_handle, current_entity + 0xCE, 4)
                
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, current_entity + 0x9E, value_bytes, len(value_bytes))    
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
           
    return "AIMBOT DRAG ON"

def RIGHTSHOULDEROFF():
    try:
        # Open the process
        proc = Pymem("HD-Player")
        
        if original_value: # check the original value is present or not
         
            for i in original_value:
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, i[0] + 0x9E, i[1], len(i[1]))
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
    return "AIMBOT DRAG OFF"


def LEFTSHOULDERON():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    
        if proc:
            global original_value
            # Save the original value to variable, btw all the orginal values are same so we just save one
            original_value = []
            for current_entity in aimbot_addresses:
                original_value.append((current_entity, read_bytes(proc.process_handle, current_entity + 0x9E, 4)))
                # Read the value at current_entity + 0x60
                # Read the value at current_entity + 0x2C
                value_bytes = read_bytes(proc.process_handle, current_entity + 0xD2, 4) 
                
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, current_entity + 0x9E, value_bytes, len(value_bytes))    
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
           
    return "AIMBOT DRAG ON"

def LEFTSHOULDEROFF():
    try:
        # Open the process
        proc = Pymem("HD-Player")
        
        if original_value: # check the original value is present or not
         
            for i in original_value:
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, i[0] + 0x9E, i[1], len(i[1]))
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
    return "AIMBOT DRAG OFF"

# def taskmanager():
#     process_name = "Taskmgr.exe"

#     try:
#         # Open the process
#         temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'task.dll')

#         dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

#         open_process = Pymem(process_name)

#         process.inject_dll(open_process.process_handle, dll_path_bytes)
#         print("Task Manager Injected DLL Successfully!") 

#     except pymem.exception.ProcessNotFound:
#         print("Task Manager not found!")
#     except Exception as e:
#         print(f"Error: {e}")

def RemoveRecoil():
    try:
       proc = Pymem("HD-Player")
    except:
        pass

    try:
       if proc:
        value = pattern_scan_all(proc.process_handle, mkp("7a 44 f0 48 2d e9 10 b0 8d e2 02 8b 2d ed 08 d0 4d e2 00 50 a0 e1 10 1a 08 ee 08 40 95 e5 00 00 54 e3"), return_multiple=True)
    except:
        pass
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("00 00"),2)


def AddRecoil():
    try:
       proc = Pymem("HD-Player")
    except:
        pass

    try:
       if proc:
        value = pattern_scan_all(proc.process_handle, mkp("00 00 f0 48 2d e9 10 b0 8d e2 02 8b 2d ed 08 d0 4d e2 00 50 a0 e1 10 1a 08 ee 08 40 95 e5 00 00 54 e3"), return_multiple=True)
    except:
        pass
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("7a 44"),2)


def box3d():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'BOX.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process_name.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Box Injected DLL Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Task Manager not found!")
    except Exception as e:
        print(f"Error: {e}")

def chamsmenu():
    process_name = "HD-Player.exe"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'charms_menu.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process_name.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Blue Injected DLL Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Task Manager not found!")
    except Exception as e:
        print(f"Error: {e}")

def chams3d():
    process_name = "HD-Player.exe"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'wallfixedchams.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process_name.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams 3D Injected DLL Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Task Manager not found!")
    except Exception as e:
        print(f"Error: {e}")


def SNIPERSCOPELOAD():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        return

    try:
        if proc:
            print("\033[31m[>]\033[0m Searching Entity...")
            # Scan for entities
            global sniperScopeAddress
            sniperScopePattern = mkp("8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 00 00 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01")
            sniperScopeAddress = pattern_scan_all(proc.process_handle, sniperScopePattern, return_multiple=True)

            if sniperScopeAddress:
                print("")
                
            else:
                print("")
    
    except:
        print("")
    finally:
        if proc:
            proc.close_process()
    return "Fitur Berhasil Di Load"

def ACTIVATELOADEDSCOPE():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    
        if proc:
            global original_Scope_value
            # Save the original value to variable, btw all the orginal values are same so we just save one
            original_Scope_value = []

            for addr in sniperScopeAddress:

                current_value = read_bytes(proc.process_handle, addr, 22)
                original_Scope_value.append(current_value)


                write_bytes(proc.process_handle, addr, bytes.fromhex("8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 F0 41 00 00 00 00 00 00 00 00"),26)

    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
           
    return "AIMBOT HEAD ON"

def REMOVELOADEDSCOPE():
    try:
        # Open the process
        proc = Pymem("HD-Player")
        
        if original_Scope_value:  # Ensure the original values exist before proceeding
            for i, original_val in enumerate(original_Scope_value):
                # Write back the original value stored in `original_value` for each address
                write_bytes(proc.process_handle, sniperScopeAddress[i], original_val, 22)
                
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
    return "AIMBOT HEAD OFF"



def SNIPERSWITCHLOAD():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        return

    try:
        if proc:
            print("\033[31m[>]\033[0m Searching Entity...")
            # Scan for entities
            global sniperSwitchAddress
            sniperSwitchPattern = mkp("5C 43 00 00 90 42 00 00 B4 42 96 00 00 00 00 00 00 00 00 00 00 3F 00 00 80 3E 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F")
            sniperSwitchAddress = pattern_scan_all(proc.process_handle, sniperSwitchPattern, return_multiple=True)

            if sniperSwitchAddress:
                print("")
                
            else:
                print("")
    
    except:
        print("")
    finally:
        if proc:
            proc.close_process()
    return "Fitur Berhasil Di Load"

def ACTIVATELOADEDSWITCH():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    
        if proc:
            global original_Switch_value
            # Save the original value to variable, btw all the orginal values are same so we just save one
            original_Switch_value = []

            for addr in sniperSwitchAddress:

                current_value = read_bytes(proc.process_handle, addr, 22)
                original_Switch_value.append(current_value)


                write_bytes(proc.process_handle, addr, bytes.fromhex("5C 43 00 00 90 42 00 00 B4 42 96 00 00 00 00 00 00 00 00 00 00 1A 00 00 80 1A"),26)

    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
           
    return "AIMBOT HEAD ON"

def REMOVELOADEDSWITCH():
    try:
        # Open the process
        proc = Pymem("HD-Player")
        
        if original_Switch_value:  # Ensure the original values exist before proceeding
            for i, original_val in enumerate(original_Switch_value):
                # Write back the original value stored in `original_value` for each address
                write_bytes(proc.process_handle, sniperSwitchAddress[i], original_val, 26)
                
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
    return "AIMBOT HEAD OFF"


def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')
    elif platform.system() == 'Linux':
        os.system('clear')
        sys.stdout.write("\x1b]0;Python Example\x07")
    # elif platform.system() == 'Darwin':
    #     os.system("clear && printf '\e[3J'")
    #     os.system('''echo - n - e "\033]0;Python Example\007"''')

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

# if sys.platform == "win32":
#     ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# def taskmanagerloop():
#     while True:
#         taskmanager()
#         print("Taskmanager is running...")
#         time.sleep(2)  # Wait for 2 seconds

# def run_taskmanager():
#     # Running taskmanagerloop in a separate thread
#     task_thread = threading.Thread(target=taskmanagerloop)
#     task_thread.daemon = True  # Allows thread to exit when the main program exits
#     task_thread.start()