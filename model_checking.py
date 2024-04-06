import bppy as bp
from bppy import BEvent, sync, SimpleEventSelectionStrategy
from bppy.analysis.dfs_bprogram_verifier import DFSBProgramVerifier
from bppy.analysis.symbolic_bprogram_verifier import SymbolicBProgramVerifier


@bp.thread
def req_1():
    while True:
        yield sync(request=BEvent("Approaching"))
        yield sync(request=BEvent("Entering"))
        yield sync(request=BEvent("Leaving"))


@bp.thread
def req_2():
    while True:
        yield sync(waitFor=BEvent("Approaching"))
        yield sync(request=BEvent("Lower"))
        yield sync(waitFor=BEvent("Leaving"))
        yield sync(request=BEvent("Raise"))


@bp.thread
def req_3():
    while True:
        yield sync(waitFor=BEvent("Approaching"))
        yield sync(block=BEvent("Entering"),
                   waitFor=BEvent("Lower"))


@bp.thread
def req_4():
    while True:
        yield sync(waitFor=BEvent("Approaching"))
        yield sync(block=BEvent("Raise"),
                   waitFor=BEvent("Leaving"))


@bp.thread
def check():
    while True:
        e = yield bp.sync(waitFor=[BEvent("Entering"), BEvent("Lower")])
        assert e == BEvent("Lower")
        yield bp.sync(waitFor=BEvent("Raise"))


def bp_gen():
    return bp.BProgram(bthreads=[req_1(), req_2(), req_3(), req_4(), check()],
                       event_selection_strategy=SimpleEventSelectionStrategy())


# initialize DFS verifier with the b-program generator and specify max_trace_length
ver = DFSBProgramVerifier(bp_gen, max_trace_length=1000)
ok, counter_example = ver.verify()

# check the verification results and print accordingly
if ok:
    print("OK")
else:
    print("Violation Found")
    print("Counterexample:")
    print(counter_example)


def init_bprogram():
    return bp.BProgram(bthreads=[req_1(), req_2(), req_3(), req_4()],
                       event_selection_strategy=SimpleEventSelectionStrategy())


ver = SymbolicBProgramVerifier(init_bprogram,
                               [BEvent("Approaching"), BEvent("Entering"), BEvent("Leaving"), BEvent("Lower"), BEvent("Raise")])

spec = "G ( (event = Approaching) -> (event != Raise U event = Leaving) )"

result, ce = ver.verify(spec=spec,
                        type="BDD",
                        find_counterexample=True)

if result:
    print("OK")
else:
    print("Violation Found")
    print("Counterexample:")
    print(ce)