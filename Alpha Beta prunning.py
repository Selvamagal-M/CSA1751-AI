import math

def alpha_beta(depth, index, is_max, scores, h, alpha, beta):
    if depth == h:
        return scores[index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, False, scores, h, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, scores, h, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    print("Result:", alpha_beta(0, 0, True, scores, 3, -math.inf, math.inf))
