inputs=[1.0,8.0,7.8,4.7]

weights=[
    [1.7,6.9,5.8,6.9],
    [4.8,9.8,-9.0,7.0],
    [0.8,-8.9,9.7,8.7],
    [-9.8,8.7,6.8,4.7],

    ]

bias=[0.7,0.5,0.9,0.1]
outputs=[]

for neuron_weights, neuron_bias in zip(weights,bias):
    total=0
    for n_input, weight in zip(inputs, neuron_weights):
         total += n_input * weight
    total+=neuron_bias

 
    outputs.append(total)

print("Layer output:", outputs)















































