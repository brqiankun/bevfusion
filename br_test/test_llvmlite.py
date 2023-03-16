from llvmlite import binding
target = binding.Target.from_default_triple()
target_machine = target.create_target_machine()