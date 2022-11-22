"""
This module is generated from the ``random`` test generator.
Please do not edit this file manually.
See the README for that generator for more information.
"""

from eth2spec.test.helpers.constants import EIP4844
from eth2spec.test.context import (
    misc_balances_in_default_range_with_many_validators,
    with_phases,
    zero_activation_threshold,
    only_generator,
)
from eth2spec.test.context import (
    always_bls,
    spec_test,
    with_custom_state,
    single_phase,
)
from eth2spec.test.utils.randomized_block_tests import (
    run_generated_randomized_test,
)


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_0(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_1(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_2(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_3(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_4(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_5(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_6(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_7(spec, state):
    # scenario as high-level, informal text:
    # epochs:0,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'validation': 'validate_is_not_leaking', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_8(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_9(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_10(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_11(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_12(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:last_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'last_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_13(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:random_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'random_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_14(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:penultimate_slot_in_epoch,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 0, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 'penultimate_slot_in_epoch', 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )


@only_generator("randomized test for broad coverage, not point-to-point CI")
@with_phases([EIP4844])
@with_custom_state(
    balances_fn=misc_balances_in_default_range_with_many_validators,
    threshold_fn=zero_activation_threshold
)
@spec_test
@single_phase
@always_bls
def test_randomized_15(spec, state):
    # scenario as high-level, informal text:
    # epochs:epochs_until_leak,slots:0,with-block:no_block
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    # epochs:1,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:no_block
    # epochs:0,slots:0,with-block:random_block_eip4844
    scenario = {'transitions': [{'epochs_to_skip': 'epochs_until_leak', 'validation': 'validate_is_leaking', 'slots_to_skip': 0, 'block_producer': 'no_block'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}, {'epochs_to_skip': 1, 'slots_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'slots_to_skip': 0, 'epochs_to_skip': 0, 'block_producer': 'no_block', 'validation': 'no_op_validation'}, {'block_producer': 'random_block_eip4844', 'epochs_to_skip': 0, 'slots_to_skip': 0, 'validation': 'no_op_validation'}], 'state_randomizer': 'randomize_state_eip4844'}  # noqa: E501
    yield from run_generated_randomized_test(
        spec,
        state,
        scenario,
    )