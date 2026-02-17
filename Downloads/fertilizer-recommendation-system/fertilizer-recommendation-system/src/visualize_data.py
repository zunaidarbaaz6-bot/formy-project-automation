"""
Data visualization module for fertilizer recommendation system
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualizer:
    """
    Create comprehensive visualizations for agricultural data analysis
    """
    
    def __init__(self, data_path='data/raw/fertilizer_data.csv'):
        self.df = pd.read_csv(data_path)
        self.setup_style()
    
    def setup_style(self):
        """Setup plotting style"""
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 10
    
    def plot_nutrient_distribution(self, save_path='reports/figures/nutrient_distribution.png'):
        """
        Plot distribution of NPK nutrients
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        
        nutrients = ['Nitrogen', 'Phosphorus', 'Potassium']
        colors = ['#2E86AB', '#A23B72', '#F18F01']
        
        for ax, nutrient, color in zip(axes, nutrients, colors):
            ax.hist(self.df[nutrient], bins=30, color=color, alpha=0.7, edgecolor='black')
            ax.set_xlabel(f'{nutrient} (kg/ha)', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            ax.set_title(f'{nutrient} Distribution', fontsize=14, fontweight='bold')
            ax.axvline(self.df[nutrient].mean(), color='red', linestyle='--', 
                      linewidth=2, label=f'Mean: {self.df[nutrient].mean():.2f}')
            ax.legend()
        
        plt.suptitle('NPK Nutrient Distribution Analysis', fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Nutrient distribution plot saved to {save_path}")
        plt.close()
    
    def plot_correlation_heatmap(self, save_path='reports/figures/correlation_heatmap.png'):
        """
        Plot correlation heatmap of features
        """
        plt.figure(figsize=(12, 10))
        
        # Select numerical columns
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        corr_matrix = self.df[numerical_cols].corr()
        
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', 
                   cmap='coolwarm', center=0, square=True,
                   linewidths=1, cbar_kws={"shrink": 0.8})
        
        plt.title('Feature Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Correlation heatmap saved to {save_path}")
        plt.close()
    
    def plot_fertilizer_distribution(self, save_path='reports/figures/fertilizer_distribution.png'):
        """
        Plot fertilizer recommendation distribution
        """
        plt.figure(figsize=(14, 7))
        
        fertilizer_counts = self.df['Fertilizer'].value_counts()
        colors = sns.color_palette('husl', len(fertilizer_counts))
        
        bars = plt.bar(range(len(fertilizer_counts)), fertilizer_counts.values, 
                      color=colors, edgecolor='black', linewidth=1.5)
        
        plt.xlabel('Fertilizer Type', fontsize=12, fontweight='bold')
        plt.ylabel('Number of Recommendations', fontsize=12, fontweight='bold')
        plt.title('Fertilizer Recommendation Distribution', fontsize=16, fontweight='bold', pad=20)
        plt.xticks(range(len(fertilizer_counts)), fertilizer_counts.index, rotation=45, ha='right')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Fertilizer distribution plot saved to {save_path}")
        plt.close()
    
    def plot_crop_analysis(self, save_path='reports/figures/crop_analysis.png'):
        """
        Plot crop-wise nutrient requirements
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # NPK by crop
        crops = self.df['Crop'].unique()
        nutrients = ['Nitrogen', 'Phosphorus', 'Potassium']
        
        for idx, nutrient in enumerate(nutrients):
            ax = axes[idx // 2, idx % 2]
            crop_data = [self.df[self.df['Crop'] == crop][nutrient].values for crop in crops]
            
            bp = ax.boxplot(crop_data, labels=crops, patch_artist=True,
                           notch=True, showmeans=True)
            
            colors = sns.color_palette('Set2', len(crops))
            for patch, color in zip(bp['boxes'], colors):
                patch.set_facecolor(color)
                patch.set_alpha(0.7)
            
            ax.set_xlabel('Crop Type', fontsize=11, fontweight='bold')
            ax.set_ylabel(f'{nutrient} (kg/ha)', fontsize=11, fontweight='bold')
            ax.set_title(f'{nutrient} Requirements by Crop', fontsize=13, fontweight='bold')
            ax.tick_params(axis='x', rotation=45)
            ax.grid(axis='y', alpha=0.3)
        
        # Crop distribution
        ax = axes[1, 1]
        crop_counts = self.df['Crop'].value_counts()
        colors = sns.color_palette('viridis', len(crop_counts))
        
        wedges, texts, autotexts = ax.pie(crop_counts.values, labels=crop_counts.index,
                                           autopct='%1.1f%%', colors=colors,
                                           startangle=90, textprops={'fontsize': 10})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Crop Distribution', fontsize=13, fontweight='bold')
        
        plt.suptitle('Crop-wise Nutrient Analysis', fontsize=16, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Crop analysis plot saved to {save_path}")
        plt.close()
    
    def plot_environmental_factors(self, save_path='reports/figures/environmental_factors.png'):
        """
        Plot environmental factors analysis
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Temperature distribution by fertilizer
        fertilizers = self.df['Fertilizer'].unique()[:5]  # Top 5 fertilizers
        data_temp = [self.df[self.df['Fertilizer'] == f]['Temperature'].values 
                    for f in fertilizers]
        
        ax = axes[0, 0]
        bp = ax.violinplot(data_temp, positions=range(len(fertilizers)), 
                          showmeans=True, showmedians=True)
        ax.set_xticks(range(len(fertilizers)))
        ax.set_xticklabels(fertilizers, rotation=45, ha='right')
        ax.set_ylabel('Temperature (°C)', fontsize=11, fontweight='bold')
        ax.set_title('Temperature Distribution by Fertilizer', fontsize=13, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        # Humidity vs Temperature scatter
        ax = axes[0, 1]
        scatter = ax.scatter(self.df['Temperature'], self.df['Humidity'],
                           c=self.df['Rainfall'], cmap='Blues', alpha=0.6, s=50)
        ax.set_xlabel('Temperature (°C)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Humidity (%)', fontsize=11, fontweight='bold')
        ax.set_title('Temperature vs Humidity (colored by Rainfall)', 
                    fontsize=13, fontweight='bold')
        plt.colorbar(scatter, ax=ax, label='Rainfall (mm)')
        
        # pH distribution
        ax = axes[1, 0]
        ax.hist(self.df['pH'], bins=25, color='#E63946', alpha=0.7, edgecolor='black')
        ax.axvline(6.5, color='green', linestyle='--', linewidth=2, label='Slightly Acidic')
        ax.axvline(7.5, color='blue', linestyle='--', linewidth=2, label='Slightly Alkaline')
        ax.set_xlabel('pH Level', fontsize=11, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
        ax.set_title('Soil pH Distribution', fontsize=13, fontweight='bold')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        # Rainfall distribution
        ax = axes[1, 1]
        ax.hist(self.df['Rainfall'], bins=25, color='#457B9D', alpha=0.7, edgecolor='black')
        ax.set_xlabel('Rainfall (mm)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
        ax.set_title('Rainfall Distribution', fontsize=13, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        plt.suptitle('Environmental Factors Analysis', fontsize=16, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Environmental factors plot saved to {save_path}")
        plt.close()
    
    def plot_npk_relationships(self, save_path='reports/figures/npk_relationships.png'):
        """
        Plot NPK nutrient relationships
        """
        fig = plt.figure(figsize=(16, 6))
        
        # Create 3D subplot for NPK relationship
        ax1 = fig.add_subplot(131, projection='3d')
        
        fertilizers = self.df['Fertilizer'].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(fertilizers)))
        
        for fertilizer, color in zip(fertilizers, colors):
            mask = self.df['Fertilizer'] == fertilizer
            ax1.scatter(self.df[mask]['Nitrogen'], 
                       self.df[mask]['Phosphorus'],
                       self.df[mask]['Potassium'],
                       c=[color], label=fertilizer, alpha=0.6, s=30)
        
        ax1.set_xlabel('Nitrogen', fontsize=10, fontweight='bold')
        ax1.set_ylabel('Phosphorus', fontsize=10, fontweight='bold')
        ax1.set_zlabel('Potassium', fontsize=10, fontweight='bold')
        ax1.set_title('NPK 3D Relationship', fontsize=12, fontweight='bold')
        
        # N-P ratio by fertilizer
        ax2 = fig.add_subplot(132)
        self.df['N_P_ratio'] = self.df['Nitrogen'] / (self.df['Phosphorus'] + 1)
        
        for fertilizer in fertilizers[:5]:
            mask = self.df['Fertilizer'] == fertilizer
            ax2.scatter(self.df[mask]['Nitrogen'], self.df[mask]['Phosphorus'],
                       label=fertilizer, alpha=0.6, s=50)
        
        ax2.set_xlabel('Nitrogen (kg/ha)', fontsize=11, fontweight='bold')
        ax2.set_ylabel('Phosphorus (kg/ha)', fontsize=11, fontweight='bold')
        ax2.set_title('Nitrogen vs Phosphorus by Fertilizer', fontsize=12, fontweight='bold')
        ax2.legend(fontsize=8)
        ax2.grid(alpha=0.3)
        
        # N-K ratio by fertilizer
        ax3 = fig.add_subplot(133)
        
        for fertilizer in fertilizers[:5]:
            mask = self.df['Fertilizer'] == fertilizer
            ax3.scatter(self.df[mask]['Nitrogen'], self.df[mask]['Potassium'],
                       label=fertilizer, alpha=0.6, s=50)
        
        ax3.set_xlabel('Nitrogen (kg/ha)', fontsize=11, fontweight='bold')
        ax3.set_ylabel('Potassium (kg/ha)', fontsize=11, fontweight='bold')
        ax3.set_title('Nitrogen vs Potassium by Fertilizer', fontsize=12, fontweight='bold')
        ax3.legend(fontsize=8)
        ax3.grid(alpha=0.3)
        
        plt.suptitle('NPK Nutrient Relationships and Patterns', 
                    fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"NPK relationships plot saved to {save_path}")
        plt.close()
    
    def generate_all_visualizations(self):
        """
        Generate all visualizations at once
        """
        print("\n" + "="*60)
        print("GENERATING DATA VISUALIZATIONS")
        print("="*60 + "\n")
        
        self.plot_nutrient_distribution()
        self.plot_correlation_heatmap()
        self.plot_fertilizer_distribution()
        self.plot_crop_analysis()
        self.plot_environmental_factors()
        self.plot_npk_relationships()
        
        print("\n" + "="*60)
        print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
        print("="*60)
        print("\nVisualizations saved to: reports/figures/")
        print("\nGenerated plots:")
        print("  1. Nutrient Distribution")
        print("  2. Correlation Heatmap")
        print("  3. Fertilizer Distribution")
        print("  4. Crop Analysis")
        print("  5. Environmental Factors")
        print("  6. NPK Relationships")


def main():
    """
    Main visualization pipeline
    """
    visualizer = DataVisualizer()
    visualizer.generate_all_visualizations()


if __name__ == "__main__":
    main()
