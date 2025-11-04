export interface ReconciliationResult {
  date: string;
  bank_balance: number;
  transaction_total_per_date: number;
  transaction_total_per_date_cumulative: number;
  transactions_per_date: number[];
  match_bool: boolean;
}

interface ApiResponse {
  results: ReconciliationResult[];
}

export const fetchReconciliationResults = async (): Promise<ReconciliationResult[]> => {
  const response = await fetch('http://localhost:8000/validate');
  
  if (!response.ok) {
    throw new Error(`Failed to fetch: ${response.statusText}`);
  }
  
  const data: ApiResponse = await response.json();
  return data.results;
};

