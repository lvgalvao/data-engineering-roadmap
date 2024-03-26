from typing import Union, Dict


GenericSchema = Dict[str, Union[str, float, int]]


CompraSchema: GenericSchema = {
    "ean" : int,
    "price" : float,
    "store" : int,
    "dateTime" : str
}