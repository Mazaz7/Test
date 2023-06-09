from pipeline_data import compute_median_mean_diff
import pytest

def test_compute_median_mean_diff():
    # Création de données de test
    data = [1, 2, 3, 4, 5]
    df = pd.DataFrame({'Value': data})

    # Calcul de la différence entre moyenne et médiane
    result = compute_median_mean_diff(df)

    # Vérification du résultat
    assert result.loc['Value', 'Diff'] == 0.0
