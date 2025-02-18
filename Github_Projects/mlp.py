import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size, dropout_rate=0.2):
        """
        Initialize Multi-Layer Perceptron
        Args:
            input_size (int): Size of input features
            hidden_sizes (list): List of hidden layer sizes
            output_size (int): Size of output
            dropout_rate (float): Dropout probability
        """
        super(MLP, self).__init__()
        
        # Create list to hold all layers
        layers = []
        
        # Input layer
        prev_size = input_size
        
        # Add hidden layers
        for hidden_size in hidden_sizes:
            layers.extend([
                nn.Linear(prev_size, hidden_size),
                nn.ReLU(),
                nn.Dropout(dropout_rate)
            ])
            prev_size = hidden_size
        
        # Add output layer
        layers.append(nn.Linear(prev_size, output_size))
        
        # Combine all layers
        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        """Forward pass"""
        return self.model(x)

# Example usage
if __name__ == "__main__":
    # Example parameters
    input_size = 784  # e.g., for MNIST
    hidden_sizes = [512, 256, 128]
    output_size = 10  # e.g., 10 classes
    batch_size = 32
    
    # Create model
    model = MLP(input_size, hidden_sizes, output_size)
    
    # Example input
    x = torch.randn(batch_size, input_size)
    
    # Forward pass
    output = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}") 