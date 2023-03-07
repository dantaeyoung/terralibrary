from say import say
import barlang
import importlib





class BarlangInterpreter:
    def __init__(self):
        self.stack = []
        self.mode = "run"

    def __str__(self):
        return f"Mode is {self.mode}. State is {self.stackstring()}"

    def to_state(self):
        return {
            "stack": self.stack,
            "mode": self.mode
        }

    def reload(self):
        importlib.reload(barlang)


    def try_to_run(self, cmd, arg=None):
        print("[CMD] ", cmd)
        thisstate = self.to_state()
        if(arg):
            thisstate['arg'] = arg  
        obj_str = repr(thisstate)
        print("[objstr] " + obj_str)
        try:
            res = eval("barlang." + cmd + "(" + obj_str + ")")
            print("[RES] " , res)
            if(res != None):
                self.stack = res['stack']
                self.mode = res['mode']

        except Exception as e:
            say("Error: " + str(e))
            print(e)


    def interpret(self, s):
        
        if(s.startswith("debug:ooga")):
            say("woweee")
            return

        helpcmd = s.replace("!", "excl_").replace("@","at_")

        if(s.startswith("#reloadbarlang")):
            say("reloading barlang")
            importlib.reload(barlang)
            return
                
        if(s.startswith("!") or s.startswith("@")):
            self.try_to_run(helpcmd)
            return

        if(s.startswith("mode:")):
            self.mode = s.split(":")[1]
            say("Mode is " + self.mode)
            return


        if(self.mode == "stack"):
            self.stack.append(s)
            say("appended " + s)
            return

        if(self.mode == "say"):
            say(s)
            return

        if(self.mode == "run"):
            ## TODO FIX
            if(len(self.stack) > 0):
                self.try_to_run(self.stack[-1], arg=s)
            else:
                say("Nothing to run!")
            return


