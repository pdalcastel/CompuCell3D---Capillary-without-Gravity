
from cc3d import CompuCellSetup
        

from capilaridadeSteppables import capilaridadeSteppable

CompuCellSetup.register_steppable(steppable=capilaridadeSteppable(frequency=1))


CompuCellSetup.run()
